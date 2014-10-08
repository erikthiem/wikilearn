import xml.etree.ElementTree as etree
import re
from collections import Counter


def getSource():
	source = 'data/enwiki-20140903-pages-articles.xml'
	return source

def getStringLead():
	sl = "{http://www.mediawiki.org/xml/export-0.9/}"
	return sl

class PageInfo:
   'Everyting you need to know about a page'
   pageCount = 0
   def __init__(self, title, text, linksAndCounts):
      self.title = title
      self.text = text
      self.linksAndCounts = linksAndCounts
      PageInfo.pageCount += 1

#depreciated--DO NOT REMOVE.  iterates through full xml
def getOrderedLinksAndCounts(desiredLinkCount):
	source = getSource() #XML to be parsed
	#source = 'data/testdata/cd_catalog.xml' #Test XML to be parsed
	stringLead = getStringLead()
	# get an iterable
	context = etree.iterparse(source, events=("start", "end"))
	# turn it into an iterator
	context = iter(context)
	# get the root element
	event, root = context.next()
	#THE FUN BEGINS
	for event, elem in context:
	    if event == "end":
		#print "Element:" + elem.tag +"\n"
		if elem.tag == stringLead + "page":
		    for child in elem:
		        #print child.tag, child.attrib
		        if child.tag == stringLead + "title":
			    print "TITLE:" + child.text
		        if child.tag == stringLead + "revision":
		            for child_of_rev in child:
		                #print "child of revision:" + child_of_rev.tag#, child_of_rev.text
				if child_of_rev.tag == stringLead + "text":
		                    text = child_of_rev.text
		                    links = re.findall(r'\[\[(.*?)\]\]', text)
		                    
		                    #print Counter(links)
		                    listMap = []
		                    for link in links:
		                        link = link.split('|')[-1]
		                        [link if x !="!@$somephraseitwillneverbe" else x for x in links]
					linkCount = links.count(link)
		                        #listMap = []
					if 1 == 1: #linkCount > desiredLinkCount-1: #add back to return less links
		                            #print link + str(linkCount)
		                            listMap.append((link, linkCount+1))
		                            while link in links: links.remove(link)
		                    sortedListMap = sorted(listMap, key=lambda link: link[1], reverse=True)
		                    for linkAndValue in sortedListMap:
                                        print linkAndValue[0] + str(linkAndValue[1])
		                    
		root.clear()
	return sortedListMap #TODO: not working now--needs to return for a SPECIFIC article

#####################################################################################################################

def getText(articleTitle): #yet to be modified //TODO:
	source = getSource() #XML to be parsed
	#source = 'data/testdata/cd_catalog.xml' #Test XML to be parsed
	stringLead = getStringLead()
	# get an iterable
	context = etree.iterparse(source, events=("start", "end"))
	# turn it into an iterator
	context = iter(context)
	# get the root element
	event, root = context.next()
	#THE FUN BEGINS
	for event, elem in context:
		if event == "end":
			if (elem.tag == stringLead + "page") and (elem.find(stringLead+'title').text == articleTitle):
				for child in elem:
					if child.tag == stringLead + "title":
						print "TITLE:" + child.text
					if child.tag == stringLead + "revision":
						for child_of_rev in child:
							if child_of_rev.tag == stringLead + "text":
				            			#print child_of_rev.text
								return elem
	return 0


################################################################################################################

def getPageInfo(page):
	source = getSource() #XML to be parsed
	#source = 'data/tesdata/cd_catalog.xml' #Test XML to be parsed
	stringLead = getStringLead()
	# get an iterable
	context = etree.iterparse(source, events=("start", "end"))
	# turn it into an iterator
	context = iter(context)
	# get the root element
	event, root = context.next()
	#THE FUN BEGINS
	for child in page:
		if child.tag == stringLead + "title":
			pageTitle = child.text #pageTitle
		if child.tag == stringLead + "revision":
			for child_of_rev in child:
				if child_of_rev.tag == stringLead + "text":
					pageText = child_of_rev.text #pageText
					links = re.findall(r'\[\[(.*?)\]\]', pageText)
					listMap = []
		                    	for link in links:
				                link = link.split('|')[-1]
				                [link if x !="!@$somephraseitwillneverbe" else x for x in links]
						linkCount = links.count(link)
						if 1 == 1: #linkCount > desiredLinkCount-1: #add back to return less links
				                    #print link + str(linkCount)
				                    listMap.append((link, linkCount+1))
				                    while link in links: links.remove(link)
					sortedListMap = sorted(listMap, key=lambda link: link[1], reverse=True)#sortedListMap
					pageInfo = PageInfo(pageTitle, pageText, sortedListMap)#------------------#
					return pageInfo
#########################################################################################
					

#MAIN
#getOrderedLinksAndCounts(1)
#page = getText('Zodiac')
page = getText('Zodiac') #getTextIsMisnamed.  It returns the whole page
pageInfo = getPageInfo(page)
print pageInfo.title
print pageInfo.text
print str(pageInfo.linksAndCounts)


#format, revision, page, title, ns, id, redirect, parentid, timestamp, username, contributor, comment, text, shal, model, format,
#

'''
revision

{http://www.mediawiki.org/xml/export-0.9/}id {}
{http://www.mediawiki.org/xml/export-0.9/}parentid {}
{http://www.mediawiki.org/xml/export-0.9/}timestamp {}
{http://www.mediawiki.org/xml/export-0.9/}contributor {}
{http://www.mediawiki.org/xml/export-0.9/}text {'{http://www.w3.org/XML/1998/namespace}space': 'preserve'}
{http://www.mediawiki.org/xml/export-0.9/}sha1 {}
{http://www.mediawiki.org/xml/export-0.9/}model {}
{http://www.mediawiki.org/xml/export-0.9/}format {}



page

{http://www.mediawiki.org/xml/export-0.9/}title {}
{http://www.mediawiki.org/xml/export-0.9/}ns {}
{http://www.mediawiki.org/xml/export-0.9/}id {}
{http://www.mediawiki.org/xml/export-0.9/}revision {}
'''







