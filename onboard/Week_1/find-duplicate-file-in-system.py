class Solution(object):
    def findDuplicate(self, paths):
      
        content_dict = {}
        
        for path in paths:
            parts = path.split(" ")
            directory = parts[0]
            
            for file_info in parts[1:]:
                file_parts = file_info.split("(")
                file_name = file_parts[0]
                file_content = file_parts[1][:-1]  
                
                if file_content not in content_dict:
                    content_dict[file_content] = []
                content_dict[file_content].append(directory + "/" + file_name)
        
        result = []
        for files in content_dict.values():
            if len(files) > 1:
                result.append(files)
        
        return result