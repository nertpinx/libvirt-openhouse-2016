#!/usr/bin/env python

import sys
import libvirt

if len(sys.argv) != 2:
    print("Usage: %s <name>" % sys.argv[0])
    sys.exit(1)

xml = """
<domain type='qemu'>
  <name>%s</name>
  <memory unit='KiB'>131072</memory>
  <vcpu placement='static'>1</vcpu>
  <os>
    <type arch='i386' machine='pc'>hvm</type>
  </os>
  <devices>
    <memballoon model='none'/>
  </devices>
</domain>
""" % sys.argv[1]

c = libvirt.open()
d = None
ret = 0

try:
    d = c.define(xml)
    print("Domain %s created successfully" % sys.argv[1])
except (libvirt.libvirtError) as e:
    print("Cannot create domain")
    ret = 1

del d
c.close()
del c

sys.exit(ret)
