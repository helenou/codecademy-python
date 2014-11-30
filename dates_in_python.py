from datetime import datetime
maintenant = datetime.now()

print '%s/%s/%s %s:%s:%s' % (maintenant.month, maintenant.day, maintenant.year, maintenant.hour, maintenant.minute, maintenant.second)
