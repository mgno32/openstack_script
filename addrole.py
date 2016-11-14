import keystoneclient.v2_0.client as ksclient
endpoint = "http://192.168.1.136:35357/v2.0"
admin_token = "ADMIN"

keystone = ksclient.Client(endpoint=endpoint, token=admin_token)
user_role = keystone.roles.create("user")
admin_role = keystone.roles.create("admin")
xiaoyu_tenant = keystone.tenants.create(tenant_name="roleMgno32",
                        description="Xiaoyu as a role.",
                        enabled=True)
admin_user = keystone.users.create(name="admin1",
                password="ADMIN",
                email="user2@example.com", tenant_id=xiaoyu_tenant.id)
keystone.roles.add_user_role(admin_user, admin_role, xiaoyu_tenant)
