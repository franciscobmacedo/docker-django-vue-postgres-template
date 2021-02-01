
from rest_framework_simplejwt.token_blacklist.management.commands.flushexpiredtokens import Command

print('\n\nDeleting Outdated Tokens...')
c = Command()
c.handle()
print('\n\nDone!\n\n')


"""
Delete models:
from rest_framework_simplejwt.token_blacklist.models import *
OutstandingToken.objects.all().delete()
"""

