#!/opt/rh/rh-python36/root/usr/bin/python
import xml.etree.ElementTree as ET
import sys

#filename = 'sample.xml'
filename = 'summary-report.xml'
lim = 0


# cmd line
#===================================
if len(sys.argv) > 1:
  filename = sys.argv[1]
if len(sys.argv) > 2:
  lim = int(sys.argv[2])

print("plotting file: " + filename)

tree = ET.parse(filename)
root = tree.getroot()

# globals
#=========================================
pv = 'PresentationValue'
pn = 'PresentationName'
char = "."
sep  = "  "
indent = 0
ignoreElems = ['displayNameKey', 'displayName']

# recursive tree printer
#=========================================
def printRecur(root, level_limit):
  """Recursively prints the tree."""
  global indent
  if root.tag in ignoreElems:
    return
  value = root.get(pv)
  name  = root.get(pn)
  if name is None:
    return
  if value is None:
    print(sep*indent,char*indent, name)
  else:
    print(sep*indent,char*indent, name, '-->', value)

  indent += 1
  if indent > level_limit:
    indent -= 1
    return
  for elem in root.getchildren():
    printRecur(elem, level_limit)
  indent -= 1

# modules to print
#=========================================
inode = []
inode.append('common'+'Part'+'Manager')
inode.append('common'+'Continuum'+'Manager')
inode.append('common'+'Interface'+'Manager')
inode.append('common'+'Dfbi'+'Manager')
inode.append('common'+'Region'+'Manager')
inode.append('common'+'Simulation'+'Tools')
inode.append('basereport'+'Report'+'Manager')
inode.append('vis'+'Scene'+'Manager')
#inode.append('common'+'Simulation'+'Geometry')
#inode.append('common'+'Solver'+'Manager')
#inode.append('common'+'Solver'+'Stopping'+'Criterion'+'Manager')
#inode.append('common'+'Representation'+'Manager')
#inode.append('basereport'+'Monitor'+'Manager')
#inode.append('post'+'Solution'+'View'+'Manager')



## loop thru all tree branches if given limit on cmd line
## otherwise, prompt user for limit each time
#=========================================
if lim > 0:
  for x in inode:
    print(" ")
    for node in root.iter(x):
      printRecur(node, lim)

else:
  for x in inode:
    print(" ")
    prompt = x+" show ? "
    showNode = int(input(prompt))
    if showNode != 0:
      for node in root.iter(x):
        printRecur(node, showNode)
