from optparse import OptionParser
from lxml import etree

optparser = OptionParser()

optparser.add_option("-m",
					 action = "store",
					 type = "choice",
					 dest = "mode",
					 help = "distributed map configuration mode",
					 choices = [ "backup" , "eviction" , "nearcache" , "default" ],
					 metavar = "backup|eviction|nearcache|default",
					 )
optparser.add_option("-b",
					 action = "store",
					 type = "int",
					 dest = "backupcount",
					 help = "backup-count",
					 metavar = "INT",
					 )

optparser.add_option("-r",
					 action = "store",
					 type = "choice",
					 dest = "readbackupdata",
					 help = "read-backup-data",
					 choices = [ "false" , "true" ],
					 metavar = "false|true",
					 )

optparser.add_option("-t",
					 action = "store",
					 type = "int",
					 dest = "timetoliveseconds",
					 help = "time-to-live-seconds",
					 metavar = "INT",
					 )
optparser.add_option("-i",
					 action = "store",
					 type = "int",
					 dest = "maxidleseconds",
					 help = "max-idle-seconds",
					 metavar = "INT",
					 )

optparser.add_option("-p",
					 action = "store",
					 type = "choice",
					 dest = "evictionpolicy",
					 help = "eviction-policy",
					 choices = [ "NONE" , "LRU" , "LFU" ],
					 metavar = "NONE|LRU|LFU",
					 )

optparser.add_option("-s",
					 action = "store",
					 type = "int",
					 dest = "maxsize",
					 help = "max-size",
					 metavar = "INT",
					 )

optparser.add_option("-e",
					 action = "store",
					 type = "int",
					 dest = "evictionpercentage",
					 help = "eviction-percentage",
					 metavar = "INT",
					 )

optparser.add_option("-d",
					 action = "store",
					 type = "int",
					 dest = "evictiondelayseconds",
					 help = "eviction-delay-seconds",
					 metavar = "INT",
					 )

optparser.add_option("-o",
					 action = "store",
					 type = "choice",
					 dest = "invalidateonchange",
					 help = "invalidate-on-change",
					 choices = [ "false" , "true" ],
					 metavar = "false|true",
					 )


(options, args) = optparser.parse_args()

xmlparser = etree.XMLParser(remove_comments=False,encoding="UTF-8")
tree = etree.parse('main/resources/hazelcast.xml', parser=xmlparser)
root  = tree.getroot()
mapnode = root.find("{http://www.hazelcast.com/schema/config}map")

if not options.mode:
	exit(1)
else:

	backupcount = mapnode.find("{http://www.hazelcast.com/schema/config}backup-count")
	readbackupdata = mapnode.find("{http://www.hazelcast.com/schema/config}read-backup-data")
	timetoliveseconds = mapnode.find("{http://www.hazelcast.com/schema/config}time-to-live-seconds")
	maxidleseconds = mapnode.find("{http://www.hazelcast.com/schema/config}max-idle-seconds")
	evictionpolicy = mapnode.find("{http://www.hazelcast.com/schema/config}eviction-policy")
	maxsize = mapnode.find("{http://www.hazelcast.com/schema/config}max-size")
	evictionpercentage = mapnode.find("{http://www.hazelcast.com/schema/config}eviction-percentage")
	evictiondelayseconds = mapnode.find("{http://www.hazelcast.com/schema/config}eviction-delay-seconds")
	invalidateonchange = mapnode.find("{http://www.hazelcast.com/schema/config}invalidate-on-change")

	backupcount.text = "1"
	readbackupdata.text = "false"
	timetoliveseconds.text = "0"
	maxidleseconds.text = "0"
	evictionpolicy.text = "NONE"
	maxsize.text = "0"
	evictionpercentage.text = "25"
	evictiondelayseconds.text = "3"
	invalidateonchange.text = "true"

	if options.mode == "backup":
		if options.backupcount and options.readbackupdata:
			backupcount.text = str( options.backupcount )
			readbackupdata.text = options.readbackupdata
		else:
			print "You should provide backup-count and read-backup-data"
	elif options.mode == "eviction":
		if options.backupcount and options.timetoliveseconds and options.maxidleseconds and \
		   		options.evictionpolicy and options.maxsize and options.evictionpercentage and \
		   		options.evictiondelayseconds:
			backupcount.text = str( options.backupcount )
			timetoliveseconds.text = str( options.timetoliveseconds )
			maxidleseconds.text = str( options.maxidleseconds ) 
			evictionpolicy.text = options.evictionpolicy
			maxsize.text = str( options.maxsize )
			evictionpercentage.text = str( options.evictionpercentage )
			evictiondelayseconds.text = str( options.evictiondelayseconds )
		else:
			print "You should provide backup-count, time-to-live-seconds, max-idle-seconds, " +\
				 					 "eviction-policy, max-size, eviction-percentage and " +\
				   					 "eviction-delay-seconds"

	elif options.mode == "nearcache":
		if options.timetoliveseconds and options.maxidleseconds and options.evictionpolicy and \
				options.maxsize and options.invalidateonchange:
			timetoliveseconds.text = str( options.timetoliveseconds )
			maxidleseconds.text = str( options.maxidleseconds ) 
			evictionpolicy.text = options.evictionpolicy
			maxsize.text = str( options.maxsize )
			invalidateonchange.text = options.invalidateonchange
		else:
			print "You should provide time-to-live-seconds, max-idle-seconds, eviction-policy, " +\
				 					 "max-size and invalidateonchange"

	tree.write('main/resources/hazelcast.xml')