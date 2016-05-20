# -*- coding: utf-8 -*-
'''
@author: Simancas80

Moves generic files from the Windows Assets directory in the AppData space to a Desktop\Wind10_Wall folder.
Output format will be to jpg. Only run for Files above 300kb and gif format.
Dupe files will be overwritten as soon as naming convention is maintained.
'''


import os
import shutil
import imghdr
import getpass

# print (os.getcwd())  # gets current dir

def Get_Assets(UserName):
    
    ''' Windows 10 Assets location/Destination Desktop'''
    UserName = getpass.getuser()

    dir_src ='C:\Users\\' + UserName + '\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'   
     
    dir_des = 'C:\Users\\' + UserName + '\Desktop\Win10_Wall'
    
    if not os.path.exists(dir_des):
        os.makedirs(dir_des)

    os.chdir(dir_src)
    NewItems =0
    OldItems = 0
    
    for file in os.listdir(dir_src):
                
        if os.path.getsize(file)> 300000:
            
            ''' Copy all Files to dir_des with the current name'''
            src_file = os.path.join(dir_src,file)
            shutil.copy (src_file,dir_des)
            
               
            ''' Sets the new File Location with the New Name'''
            new_name = '{}.{}'.format(file[0:10],'jpg')      
            des_file = os.path.join(dir_des,file)
            new_des_file = os.path.join(dir_des,new_name)
            
            '''Renames the newly created files in the new location. If they exist, the duplicate file will be removed and renamed.'''
            try:
                os.rename (des_file,new_des_file)
                
                ''' Detecting if file is jpg, not based on the name.'''
                IsImg = imghdr.what(new_des_file)                 
                if IsImg == 'gif':
                    os.remove(new_des_file)
                    NewItems = NewItems -1
                
                NewItems = NewItems +1
            except WindowsError:
               os.remove(new_des_file) 
               os.rename (des_file,new_des_file)
               OldItems = OldItems + 1
               
    print 'Transfer Completed: New - {}/{}'.format (NewItems ,NewItems + OldItems)
    
def RenameFiles(UserName):
    
    
    directory = 'C:\Users\\' + UserName + '\Desktop'
    os.chdir(directory)

    
    for file in os.listdir(directory):
        print (file)
        new_name = '{}.{}'.format(file[0:10],'jpg')
        print (new_name)
        os.rename (file,new_name) 

if __name__ == '__main__':
     UserName = getpass.getuser()
     Get_Assets(UserName)
     