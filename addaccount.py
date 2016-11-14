import keystoneclient.v2_0.client as ksclient
# Replace the method arguments with the ones from your local config
keystone = ksclient.Client(auth_url="http://192.168.1.136:35357/v2.0",
                           username="admin",
                           password="admin",
                           tenant_name="demo")
glance_service = keystone.services.create(name="glance",
                            service_type="image",
                            description="OpenStack Image Service")
