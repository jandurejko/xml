import xml.etree.cElementTree as ET

tree = ET.ElementTree(file='2.xml')
tree2 = ET.ElementTree(file='3.xml')
root2 = tree2.getroot()
root = tree.getroot()
namespaces = {'tns' : 'http://localhost/schemas/GULF/2014-03'}
fail1Jada = []
fail2Jada = []
fail3Jada = []
fail4Jada = []

for id in root.findall('.//tns:ItemDetails', namespaces):
    device = id.find('tns:Device_Serial_No', namespaces)
    fail1Jada.append(device.text)

for id in root2.findall('.//tns:ItemDetails', namespaces):
    device = id.find('tns:Device_Serial_No', namespaces)
    fail2Jada.append(device.text)

print(fail1Jada)
print()
print(fail2Jada)
differencce = set(fail1Jada) & set(fail2Jada)
print(differencce)
