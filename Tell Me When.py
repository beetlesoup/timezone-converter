import pytz
from openerp import SUPERUSER_ID

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# get user's timezone
user_pool = self.pool.get('res.users')
user = user_pool.browse(cr, SUPERUSER_ID, uid)
tz = pytz.timezone(user.context_tz) or pytz.utc

# get localized dates
localized_datetime = pytz.utc.localize(datetime.datetime.strptime(utc_datetime,DATETIME_FORMAT)).astimezone(tz)

# To convert to user's timezone: 
LocalizedDate = fields.datetime.context_timestamp(cr, uid, DateInUTC, context=context)
