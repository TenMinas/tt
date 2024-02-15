from arango import ArangoClient

client = ArangoClient(hosts='https://adb.dekaminas.com')
timesheet_db = client.db('tt', username='hidden', password='hidden')

tt_config_coll = timesheet_db.collection('tt_config')



daily_ts_coll = timesheet_db.collection('daily_ts')

