import requests
import json

##Site WAN Interface Creation

Tenant="Enter Tenant ID"
Site="EnterSite ID"
AUTHToken="Enter Auth Token"
NetworkID="Enter Network ID"

url = "https://api.elcapitan.cloudgenix.com/v2.7/api/tenants/{}/sites/{}/waninterfaces".format(Tenant, Site)

payload = json.dumps({
    "bfd_mode": "aggressive",
    "bw_config_mode": "manual",
    "bwc_enabled": True,
    "cost": 128,
    "description": None,
    "label_id": "14909391661000226",
    "link_bw_down": 30,
    "link_bw_up": 10,
    "lqm_config": None,
    "lqm_enabled": True,
    "network_id": NetworkID,
    "tags": None,
    "type": "publicwan",
    "use_for_application_reachability_probes": None,
    "use_for_controller_connections": None,
    "use_lqm_for_non_hub_paths": None,
    "vpnlink_configuration": None,
    "name": "AWS Label"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'x-auth-token': AUTHToken
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

