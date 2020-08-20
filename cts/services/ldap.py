from ldap3 import Server, Connection, ALL, NTLM



LDAP_URL = '192.168.29.42'
domain = 'vikysol'

# Check user authentication in the LDAP and return his information
def get_LDAP_user(username, password):
    try:
        server = Server(LDAP_URL, get_info=ALL)
        connection = Connection(server,user='%s\\%s' % (domain, username), password=password,authentication=NTLM, auto_bind=True)
        connection.search('cn={username},ou=desktopusers,dc=vikysol,dc=com'.format(username=username),'(objectclass=person)')

        if len(connection.response) == 0:

            return None
        # test = connection.extend.standard.who_am_i()
        # print(test)
        # test2 = connection.bind()
        # print(test2)
                #session['username'] = username
        return connection.response[0]



    except:
        return None


# username = 'cn=admin,dc=example,dc=com'
# server = Server(LDAP_URL,get_info=ALL,use_ssl=True)
# server = Server(LDAP_URL,get_info=ALL)
# print(server)
# username = 'viky'
# fuser = r"vikysol\\" + username
# domain = 'vikysol'
# connection = Connection(server, user="vikysol\\viky",password='pass@123',authentication=NTLM, auto_bind=True)
# connection = Connection(server, user='%s\\%s' % (domain, username),password='pass@123',authentication=NTLM, auto_bind=True)
# conn = Connection(LDAP_URL, user='example\read-only-admin',password='password',authentication=NTLM,auto_bind=True)
# conn = Connection(LDAP_URL, 'cn=read-only-admin, dc=example, dc=com', password='password',auto_bind=True)
# conn.start_tls()
# print(conn)
# mxr = username
# connection.search('cn={mxr},ou=desktopusers,dc=vikysol,dc=com'.format(mxr=mxr),'(objectclass=person)')
# print(connection.response)
# x = get_LDAP_user(username='euler',password='password')
# print(x)

# working code

# LDAP_URL = 'ldap.forumsys.com'

# Check user authentication in the LDAP and return his information
# def get_LDAP_user(username, password):
#     try:
#         server = Server(LDAP_URL, get_info=ALL)
#         connection = Connection(server,
#                                 'uid={username},dc=example,dc=com'.format(
#                                     username=username),
#                                 password, auto_bind=True)
#
#         connection.search('dc=example,dc=com', '({attr}={login})'.format(
#             attr='uid', login=username), attributes=['cn'])
#
#         if len(connection.response) == 0:
#             return None
#
#         return connection.response[0]
#     except:
#         return None

# test = get_LDAP_user(username='viky',password='pass@123')
# print(test)