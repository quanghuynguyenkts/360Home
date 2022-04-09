from Autodesk.Revit.DB import Transaction, BuiltInParameterGroup,Category,BuiltInCategory


# Get UIDocument
uidoc = __revit__.ActiveUIDocument

# Get Document 
doc = uidoc.Document

# Get Application
app = doc.Application

file = app.OpenSharedParameterFile()
if file:
    myGroups = file.Groups
    dicta={}
    myDefinitions = []
    for a in myGroups:
        dicta[a.Name] = [b.Name for b in a.Definitions]
        group = myGroups[a.Name]
        for b in group.Definitions:
           
            definition = group.Definitions[b.Name]
            # print(definition)
            # print(b.Name)
            myDefinitions.append(definition)
    

    categories = []

    categories.append(Category.GetCategory(doc,BuiltInCategory.OST_ProjectInformation))

    catSet = doc.Application.Create.NewCategorySet()
    for cat in categories:

        if cat.AllowsBoundParameters:
            catSet.Insert(cat)

    trans = Transaction(doc, "Create Project Information Parameter")

    trans.Start()
    binding = doc.Application.Create.NewInstanceBinding(catSet)
    for definition in myDefinitions:
        doc.ParameterBindings.Insert(definition, binding, BuiltInParameterGroup.PG_DATA)
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