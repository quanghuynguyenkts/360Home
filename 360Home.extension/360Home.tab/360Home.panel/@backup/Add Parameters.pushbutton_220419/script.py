from Autodesk.Revit.DB import Transaction, BuiltInParameterGroup,Category,BuiltInCategory

from pyrevit import forms

# Get UIDocument
uidoc = __revit__.ActiveUIDocument

# Get Document 
doc = uidoc.Document

# Get Application
app = doc.Application

# items = ['item1', 'item2', 'item3']
#result  = forms.SelectFromList.show(items, button_name='Select Item',multiselect = True)

file = app.OpenSharedParameterFile()
if file:
    myGroups = file.Groups
    dicta={}
    myDefinitions = []
    for a in myGroups:
        dicta[a.Name] = [b.Name for b in a.Definitions]
        for b in a.Definitions:
            myDefinitions.append(b)
        # group = myGroups[a.Name]
        # for b in group.Definitions:
        #     definition = group.Definitions[b.Name]
        #     myDefinitions.append(definition)
        # defName = []
        # for e in myDefinitions:
        #     defName.append(e.Name)

    result  = forms.SelectFromList.show(dicta, button_name='Select Item',multiselect = True)

    # result => string

    listSelectedDefinition = []
    if result:

        for b in myDefinitions:
            if b.Name in result:
                listSelectedDefinition.append(b)
    
        categories = []

        categories.append(Category.GetCategory(doc,BuiltInCategory.OST_ProjectInformation))

        catSet = doc.Application.Create.NewCategorySet()
        for cat in categories:

            if cat.AllowsBoundParameters:
                catSet.Insert(cat)

        trans = Transaction(doc, "Create Project Information Parameter")

        trans.Start()
        binding = doc.Application.Create.NewInstanceBinding(catSet)
        for definition in listSelectedDefinition:
            doc.ParameterBindings.Insert(definition, binding, BuiltInParameterGroup.PG_IDENTITY_DATA)
        trans.Commit()





#     print(dicta)
#     # group = myGroups("1_Thong-tin-chung")
#     group = myGroups["0_Thong-tin-chung"]
#     print(group.Definitions)
   
#     definition = group.Definitions["360Home_MaDuAn"]

# categories = []

# categories.append(Category.GetCategory(doc,BuiltInCategory.OST_ProjectInformation))

# catSet = doc.Application.Create.NewCategorySet()
# for cat in categories:

#     if cat.AllowsBoundParameters:
#         catSet.Insert(cat)

# trans = Transaction(doc, "Create Project Information Parameter")

# trans.Start()
# binding = doc.Application.Create.NewInstanceBinding(catSet)
# doc.ParameterBindings.Insert(definition, binding, BuiltInParameterGroup.PG_DATA)
# trans.Commit()