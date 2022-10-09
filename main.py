import transitions as tr

if tr.dfa.accepts_input('from django.conf import settings'):
    print('accepted')
else:
    print('rejected')