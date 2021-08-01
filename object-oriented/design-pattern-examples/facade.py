# -- CLASS DEFINITIONS  -----------------------------------------------------

class MediaLibrary:
    
    def __init__(self):
        self.__mediaItems = []
    
    def __iter__(self):
        return iter(self.__mediaItems)
    
    def __str__(self):
        return '\n'.join(self.__mediaItems)
        
    def addMediaItem(self, item):
        self.__mediaItems.append(item)
        
    def delMediaItem(self, item):
        self.__mediaItems.remove(item)
            
    def getMediaItems(self):
        return self.__mediaItems

    
class BlogEditor:
    
    def __init__(self):
        self.__posts = []
        
    def __iter__(self):
        return iter(self.__posts)
    
    def __str__(self):
        return '\n'.join(self.__posts)
        
    def addPost(self, post):
        self.__posts.append(post)
        
    def delPost(self, post):
        self.__posts.remove(post)
        
    def getPosts(self):
        return self.__posts

class PluginEditor:
    
    def __init__(self):
        self.__plugins = []
        
    def __iter__(self):
        return iter(self.__plugins)
    
    def __str__(self):
        return '\n'.join(self.__plugins)
        
    def addPlugin(self, plugin):
        self.__plugins.append(plugin)
        
    def delPlugin(self, plugin):
        self.__plugins.remove(plugin)
        
    def getPlugins(self):
        return self.__plugins
    
class CommentLibrary:
    
    def __init__(self):
        self.__comments = []
        
    def __iter__(self):
        return iter(self.__comments)
    
    def __str__(self):
        return '\n'.join(self.__comments)
        
    def approveComment(self, comment):
        self.__comments.append(comment)
        
    def rejectComment(self, comment):
        self.__comments.remove(comment)
        
    def getComments(self):
        return self.__comments
        
class PageEditor:
    
    def __init__(self):
        self.__pages = []
        
    def __iter__(self):
        return iter(self.__pages)
    
    def __str__(self):
        return '\n'.join(self.__pages)
        
    def addPage(self, page):
        self.__pages.append(page)
        
    def delPage(self, page):
        self.__pages.remove(page)
        
    def getPages(self):
        return self.__pages
    

    
class AdminUI:
    
    def __init__(self):
        self.__pageEditor = PageEditor()
        self.__blogEditor = BlogEditor()
        self.__mediaLibrary = MediaLibrary()
        self.__commentLibrary = CommentLibrary()
        self.__pluginEditor = PluginEditor()
        self.__isAuthenticated = False
        self.__isEditing = False
        
    def setIsAuthenticated(self, isAuthenticated):
        self.__isAuthenticated = isAuthenticated
        
    def setIsEditing(self, isEditing):
        self.__isEditing = isEditing
        
    #----- add methods
    
    def addPage(self, page):
        self.__pageEditor.addPage(page)
        
    def addPost(self, post):
        self.__blogEditor.addPost(post)
        
    def addMediaItem(self, mediaItem):
        self.__mediaLibrary.addMediaItem(mediaItem)
    
    def approveComment(self, comment):
        self.__commentLibrary.approveComment(comment)
        
    def addPlugin(self, plugin):
        self.__pluginEditor.addPlugin(plugin)
        
    #----- delete methods
        
    def delPage(self, page):
        self.__pageEditor.delPage(page)
        
    def delPost(self, post):
        self.__blogEditor.delPost(post)
        
    def delMediaItem(self, mediaItem):
        self.__mediaLibrary.delMediaItem(mediaItem)
    
    def rejectComment(self, comment):
        self.__commentLibrary.rejectComment(comment)
        
    def delPlugin(self, plugin):
        self.__pluginEditor.delPlugin(plugin)
    
    #----- accessor methods
    
    def getPages(self):
        self.__pageEditor.getPages()
        
    def getPosts(self):
        self.__blogEditor.getPosts()
        
    def getMediaItems(self):
        self.__mediaLibrary.getMediaItems()
    
    def getComments(self):
        self.__commentLibrary.getComments()
        
    def getPlugins(self):
        self.__pluginEditor.getPlugins()

    
    def getStatus(self):
        print("Posts: ", self.getPosts())
        print("Pages: " + str(self.getPages()))
        print("Media Items: " + str(self.getMediaItems()))
        print("Plugins: " + str(self.getPlugins()))
        print("Comments: " + str(self.getComments()))
        print("Admin is logged in: " + str(self.__isAuthenticated))
        print("Admin is editing: " + str(self.__isEditing))

# -- DRIVER APPLICATION -----------------------------------------------------

def main():
    
    blogAdminUi = AdminUI()
    
    print("Logging in")
    blogAdminUi.setIsAuthenticated(True)
    blogAdminUi.getStatus()

    print("Adding a post")
    blogAdminUi.setIsEditing(True)
    blogAdminUi.addPost('this is a new post')
    blogAdminUi.getStatus()    

    print("Adding a page")
    blogAdminUi.setIsEditing(True)
    blogAdminUi.addPage('this is a new page')
    blogAdminUi.getStatus()
    
    blogAdminUi.setIsEditing(False)

    print("Approving a comment")
    blogAdminUi.approveComment('I like your post')
    blogAdminUi.getStatus() 

    print("Adding a plugin")
    blogAdminUi.addPlugin('Jetpack')
    blogAdminUi.getStatus()
    
    print("Adding a media item")
    blogAdminUi.addMediaItem('my-image.jpg')
    blogAdminUi.getStatus()    

    print("Add another post")
    blogAdminUi.addPost('this is a different post')
    blogAdminUi.getStatus() 

main()
    