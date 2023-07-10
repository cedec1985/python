def addition(*args):
    return(sum(args))
print(addition(5,2,6,10))
def invites(invite_vip,*args):
    print ('{}est un vip'.format(invite_vip))
    for invite in args:
        print('{} est un invite normal'.format(invite))
invites('paul','pierre','marie','max')
def invitées(invite_vip,*args,**kwargs):
    print('{} est un vip'.format(invite_vip))
    for invite in args:
        print('{} est un invité normal'.format(invite))
    indesirables=kwargs.get('indesirable')
    if indesirables:
        print('ces invites sont indesirables:{}'.format(','.join(indesirables)))
invitées('paul','pierre','marie','max',indesirable=['simon','jean','julie'])
