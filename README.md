# python-post.ir
A django-based service that calls post.ir soap API services

Iran Post Company provides some web-apis which is based on saop protocol to be used by other companies in order to service their customers.
Apis such calcuating postage price, generating barcode for their customers, tracking postage packet and so on.

This service is a Django web framework using celery (for async call of post services) and rest framework.

Api calls provided by this service are as follows:
    
    getcity
    CalculatePrice
    getMassBarcode24
    PushConstContractParcels
    PushVariableContractParcels
    
    


