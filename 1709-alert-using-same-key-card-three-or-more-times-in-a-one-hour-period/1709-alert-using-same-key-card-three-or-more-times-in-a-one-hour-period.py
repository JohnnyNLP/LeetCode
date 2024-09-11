class Solution(object):
    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """

        def convert_to_minutes(time_list):
            result = []
            for time in time_list:
                h, m = int(time.split(':')[0]), int(time.split(':')[1])
                result.append(60*h+m)
            return sorted(result)

        def usage_time_checker(time_list):
            if len(time_list) < 3 : return False
            else:
                for idx, time in enumerate(time_list[:-2]):
                    time_window = time+60
                    if time_list[idx+2] <= time_window :
                        return True

        # Group times by names
        keyDict = {}
        for idx, name in enumerate(keyName):
            try :
                keyDict[name].append(keyTime[idx])
            except :
                keyDict[name] = [keyTime[idx]]
        
        # Convert time to integer and check for 3 consecutive usage
        alert = []
        for key, value in keyDict.items():
            keyDict[key] = convert_to_minutes(value)
            if usage_time_checker(keyDict[key]): alert.append(key)

        print(keyDict)
        return sorted(alert)