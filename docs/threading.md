# Taegis SDK for Python

## Threading

The Python SDK supports built-in threading support.  The primary way to work with differing API call configurations is to use the service context manager with the `with service():` manager.  These should be used within the threaded function, but any change that could be applied to all running threads may be applied outside the code block where the threads are submitted.

Constructing the service object outside of the threads allows the SDK to create and share the specific service objects and GraphQL schemas between threads.  This can result in major time savings for complex interactions.

```python
from taegis_sdk_python import GraphQLService
import concurrent.futures

service = GraphQLService(environment="charlie")

def threaded_function(service: GraphQLService, tenant_id: str):
    results = []

    try:
        # this will be constrained to just the the thread
        # this will apply to all API calls within the context manager
        with service(tenant_id=tenant_id):
            # these can be ANY API calls that you want to thread
            results.append(service.subjects.query.current_subject())
            
            # the context manager can remain layered where you may want to request
            # fields specific to an API call
            with service(output="field fields { field field }")
                results.append(service.clients.query.clients())
            
            results.append(service.tenants.query.assignable_services())
    except Exception as exc:
        print(exc)
        return []
    
    return results

tenants = get_tenants() # defined elsewhere
future_results = {}
# The GraphQLService optionally supports shared configuration between threads.
# The below example supplies a user-managed token at the service level,
# which will be applied to all threads within the service,
# rather than requiring the user to supply the same token to each function.
with service(access_token=my_managed_token): # Optional
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(threaded_function, service, tenant.id): tenant.id
            for tenant in tenants
        }

        print("Completing futures...")
        for future in concurrent.futures.as_completed(futures):
            # stitch results per tenant
            tenant = futures[future]
            future_results[tenant] = future.result()
```

## Example

This example was designed to measure the new performance metrics, but does showcase the primary use case
for threading, where multiple queries are run against a large list of tenants can be setup.

```python
from taegis_sdk_python import GraphQLService
from taegis_sdk_python.services.tenants.types import TenantsQuery, Tenants

import concurrent.futures
import threading
from collections import Counter

service = GraphQLService()
production_environments = ["production", "delta", "echo", "foxtrot"]


def get_tenants(service: GraphQLService) -> List[Tenants]:
    max_results = 1000
    page_number = 1

    result = service.tenants.query.tenants(
        TenantsQuery(
            max_results=max_results,
            page_num=page_number,
        )
    )

    results = [result]

    while result.has_more:
        page_number += 1
        print(f"Polling page: {page_number}")

        result = service.tenants.query.tenants(
            TenantsQuery(
                max_results=max_results,
                page_num=page_number,
            )
        )
        results.append(result)

    return [
        tenant
        for result in results
        for tenant in result.results
    ]

def create_test_tenants_list(tenants: List[Tenants]) -> List[Tenants]:
    def single_production_enabled(environments):
        return len([
            True 
            for environment in environments 
            if environment.enabled and environment.name in production_environments
        ]) == 1

    test_tenants = []
    counter = Counter()
    for tenant in tenants:
        # finding tenants enabled in only a single environment so we don't have to verify which is the primary
        if single_production_enabled(tenant.environments):
            environment = [
                environment.name
                for environment in tenant.environments
                if environment.enabled == True and environment.name in production_environments
            ][0]

            # limit each environment to 100 tenants for consistency testing between environments
            if counter[environment] < 100:
                counter.update([environment])
                test_tenants.append(tenant)

    return test_tenants

def threaded_function(service: GraphQLService, tenant):
    results = []

    environment = [
        environment.name
        for environment in tenant.environments
        if environment.enabled == True and environment.name in production_environments
    ][0]

    try:
        with service(tenant_id=tenant.id, environment=environment):
            # these can be ANY API calls that you want to thread
            results.append(service.subjects.query.current_subject())
            results.append(service.clients.query.clients())
            results.append(service.tenants.query.assignable_services())
    except Exception as exc:
        print(exc)
        return []
    
    return results

tenants = get_tenants(service)
test_tenants = create_test_tenants_list(tenants)

future_results = {}
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = {
        executor.submit(threaded_function, service, tenant): tenant.id
        for tenant in test_tenants
    }

    print("Completing futures...")
    for future in concurrent.futures.as_completed(futures):
        # stitch results per tenant
        tenant = futures[future]
        future_results[tenant] = future.result()

# do something with future_results
```
