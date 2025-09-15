terraform {  
    required_providers {  
        harness = {  
            source = "harness/harness"
        }  
    }  
}

provider "harness" {  
    endpoint   = "https://workshop.harness.io"  
    account_id = "IFG41DWvSnaRLOVNB2uesg"  
    platform_api_key    = "pat.IFG41DWvSnaRLOVNB2uesg.68be82d448280c7349471d86.8WiU4yLFbCec1VKrQOak"  
}

# provider "harness" {
#   endpoint         = "https://app.harness.io/gateway"
#   account_id       = "...."
#   platform_api_key = "......"
# }