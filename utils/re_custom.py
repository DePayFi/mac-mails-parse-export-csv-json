import re

def custom_re_search(df_original,search_col,re_list):
    na_values = "" 
    search_content = df_original[search_col].str.lower()
    # loop: each item of a column row-wise
    matches = []
    for val in search_content:
        pass
        
        # loop: does one of the regex'es match the content? 
        for idx,match_item in enumerate(re_list):
            matched = na_values
            if str(val) == "nan":
                    self.matched_lst.append(matched)
                    break
                    
            try:
                print(idx,str(val))
                # matched is of type re.Match in case it matched. It can match only one item though and will be a str (not a list!) in that case
                matched = re.search(r'^([Rr]e:.)?{custom_re}$'.format(custom_re = re_item[0]), val,re.IGNORECASE)
            except Exception as e:
                print("re.search failed with Exception:",e,"\nfield: ",val)
                matched = na_values
                continue
                #a regex matched the content
            if type(matched) == re.Match:
                    groups = len(matched.span())
                    if groups > 0:
                        matched = matched.group(groups).strip()
                        self.matched_lst.append(matched)
                        break
            if idx == len(re_list)-1:
                    print("appending")
                    matches.append(matched)
                    print("done")
    return matches
