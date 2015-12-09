from xml.dom import minidom

doc=minidom.Document()
doc.appendChild(doc.createComment("this is a simple xml"))
booklist=doc.createElement("booklist")
doc.appendChild(booklist)


def addBook(newbook):
      book=doc.createElement("book")
      book.setAttribute('id',newbook['id'])

      title=doc.createElement('title')
      title.appendChild(doc.createTextNode(newbook['title']))
      book.appendChild(title)

      author=doc.createElement('author')
      name=doc.createElement('name')

      firstname=doc.createElement('firstname')
      lastname=doc.createElement('lastname')

      firstname.appendChild(doc.createTextNode(newbook['firstname']))
      lastname.appendChild(doc.createTextNode(newbook['lastname']))

      name.appendChild(firstname)
      name.appendChild(lastname)

      author.appendChild(name)
      book.appendChild(author)

      pubdate=doc.createElement('pubdate')
      pubdate.appendChild(doc.createTextNode(newbook['pubdate']))
      book.appendChild(pubdate)
      booklist.appendChild(book)
      
addBook({"id":"1001","title":"An apple","firstname":"Peter",
         "lastname":"Zhang","pubdate":"2012-1-12"})
addBook({"id":"1003","title":"Steve.Jobs","firstname":"Tom",
         "lastname":"Wang","pubdate":"2012-1-19"})
addBook({"id":"1004","title":"Harry Potter","firstname":"Peter",
         "lastname":"Chen","pubdate":"2012-11-11"})

#f=open('book.xml','w')
#doc.writexml(f)
#f.close()


class bookreader(object):
      def __init__(self,doc):
            for child in doc.childNodes:
                  if child.nodeType==doc.ELEMENT_NODE and \
                  child.tagName=='book':
                        bookid=child.getAttribute('id')
                        print("*"*20)
                        print("book id :" +bookid)
                        self.handle_book(child)

      def handle_book(self,node):
            for child in node.childNodes:
                  if child.nodeType==doc.ELEMENT_NODE:
                        if child.tagName=='title':
                              print("title: "+self.getText(child))
                        elif child.tagName=='author':
                              self.handle_author(child)
                        elif child.tagName=='pubdate':
                              print("pubdate: "+self.getText(child))
      def getText(self,node):
            child=node.firstChild
            if child.nodeType== doc.TEXT_NODE:
                  return child.nodeValue
            else:
                  return ''
      def handle_author(self,node):
            name=node.firstChild
            for child in name.childNodes:
                  if child.nodeType== doc.ELEMENT_NODE:
                        if child.tagName== 'firstname':
                              print('firstname:'+self.getText(child))
                        elif child.tagName=='lastname':
                              print('lastname:'+self.getText(child))

            

doc=minidom.parse('book.xml')
for child in doc.childNodes:
      if child.nodeType== doc.COMMENT_NODE:
            print("Comment:"+child.nodeValue)
      elif child.nodeType== doc.ELEMENT_NODE and child.tagName=='booklist':
            bookreader(child)











