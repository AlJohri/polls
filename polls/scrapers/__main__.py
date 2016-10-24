from . import RCPCurrent, HPCurrent, DKOSCurrent, QuinnipiacCurrent, PPPCurrent

# Aggregators

print "\nRCP"; 		  RCPCurrent.download()
print "\nHP";  		  HPCurrent.download()
print "\nDKOS"; 	  DKOSCurrent.download()

# Sources

print "\nQuinnipiac"; QuinnipiacCurrent.download()
print "\nPPP"; 		  PPPCurrent.download()

