import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class dsNode():
    def __init__(self, feature_idx=None, threshold=None, left=None, right=None, info_gain=None, value=None):

        self.feature_idx = feature_idx #index har feature ya vijgi
        self.threshold = threshold #meghdar har feature be ezay node asli joda konanade
        self.left = left  #bache samt chap
        self.right = right #bache samt rast
        self.info_gain = info_gain  
        
        # for leaf node
        self.value = value
class DecisionTree():
    def __init__(self, min_samples=2, max_depth=2):
        
        # meghdardehi rishe derakht
        self.root = None
        
        # sharayeti baray tavaghof sakhtan derakht ta derakhtemon kheili bozorg nashe
        self.min_samples = min_samples
        self.max_depth = max_depth
        
    def build_tree(self, dataset, current_depth=0):
        #tabe besorat bazgashti derakht tasmim ra misazad
        
        X, Y = dataset[:,:-1], dataset[:,-1] # feature ha va on meghdar outcome ra az dade ha joda mikonad
        num_samples, num_features = np.shape(X) # avali teada kol nemone ha va dovomi tedad vijgi ha mibashad
        
        # ebteda sharayet tavaghof sakhtan derakht ra check mikonad
        if num_samples>=self.min_samples and current_depth<=self.max_depth:
            # beharin split ra ba estefade az tabe marbote peyda mikonad
            split_dict = self.best_split(dataset, num_samples, num_features)
            # az onjaie ke meghdar info_gain dar ebteday kar menha infinity mibashad pas chek mikonad ke agar mosbat ast
            if split_dict["info_gain"]>0:
                # betor bazgashti samt chap
                left_subtree = self.build_tree(split_dict["dataset_left"], current_depth+1)
                # betor bazgashti samt rast
                right_subtree = self.build_tree(split_dict["dataset_right"], current_depth+1)
                # return node ra ba etelat jadid bedast amade
                return dsNode(split_dict["feature_index"], split_dict["threshold"], 
                            left_subtree, right_subtree, split_dict["info_gain"])
        
        # compute leaf node
        leaf_value = self.calculate_leaf_value(Y)
        # return leaf node
        return dsNode(value=leaf_value)
    
    def best_split(self, dataset, num_samples, num_features):   
        # dictionary baray zakhire kardan behtarin split ke daray key hay: 1.feature_index 2.threshold 3.dataset_left 4.dataset_right 5.info_gain
        best_split = {}
        max_info_gain = -1000
        
        # ro index hame feature ha for mizanim
        for feature_index in range(num_features):
            feature_values = dataset[:, feature_index] #value hay on feature
            possible_thresholds = np.unique(feature_values) # meghdar unique on value ha
            # roy value hay unique on feature ha for mizanim
            for threshold in possible_thresholds:
                # bar asas on value split mikonim
                dataset_left, dataset_right = self.split(dataset, feature_index, threshold)
                # check mikonim ke bache hash null nabashan
                if len(dataset_left)>0 and len(dataset_right)>0:
                    y, left_y, right_y = dataset[:, -1], dataset_left[:, -1], dataset_right[:, -1] # baray bache hay samt rast va chap feature ha va outcome ro dobare joda mikonim
                    # information gain ro baray meghdar jadid hesab mikonim
                    curr_info_gain = self.information_gain(y, left_y, right_y)
                    # agar information gain ke dobare hesab kardim az ghabliya behtar bashe jadid ro jaygozin mikonim
                    if curr_info_gain>max_info_gain:
                        best_split["feature_index"] = feature_index
                        best_split["threshold"] = threshold
                        best_split["dataset_left"] = dataset_left
                        best_split["dataset_right"] = dataset_right
                        best_split["info_gain"] = curr_info_gain
                        max_info_gain = curr_info_gain
                        
        return best_split
    
    def split(self, dataset, feature_index, threshold):
        # check mikone agar value be ezay har nemone az on treshold ke roy node asli ghaara dare kamtar bood bere bache samt chap ya bishtar bood bere rast
        dataset_left = np.array([row for row in dataset if row[feature_index]<=threshold])
        dataset_right = np.array([row for row in dataset if row[feature_index]>threshold])
        return dataset_left, dataset_right
    
    def information_gain(self, parent, l_child, r_child): 
        weight_l = len(l_child) / len(parent) #baray mohasebe miyangin vazni, tedad bache hay chap be kol bache ha
        weight_r = len(r_child) / len(parent) #baray mohasebe miyangin vazni, tedad bache hay rast be kol bache ha
        gain = self.entropy(parent) - (weight_l*self.entropy(l_child) + weight_r*self.entropy(r_child)) # formol mohasebe info gain
        return gain
    
    def entropy(self, y):
        class_labels = np.unique(y)
        entropy = 0
        for cls in class_labels:
            p_cls = len(y[y == cls]) / len(y) # tedad value hayi ba on meghdar taghsim bar kol value ha darvaghe pi
            entropy += -p_cls * np.log2(p_cls)
        return entropy
    
        
    def calculate_leaf_value(self, Y):
        #dar node barg ha ke dige be split kardan edame nemidahim tedad sample ha ro negah midarim       
        Y = list(Y)
        return max(Y, key=Y.count) # on key darvaghe maximum bar aasa teda aza ro barmigardone
    
    def print_tree(self,feature_list, tree=None, indent=" "  ):
        
        if not tree:
            tree = self.root

        if tree.value is not None:
            print(tree.value)

        else:
            print("X : "+feature_list[tree.feature_idx], "<=", tree.threshold, "with information gain = ", tree.info_gain)
            print("%sleft:" % (indent), end="")
            self.print_tree(feature_list,tree.left, indent + indent)
            print("%sright:" % (indent), end="")
            self.print_tree(feature_list,tree.right, indent + indent)
    
    def fit(self, X, Y):
        #tabe baray sakhtan derakht bar asa dade hay train va train kardan dede hay train
        dataset = np.concatenate((X, Y), axis=1)
        self.root = self.build_tree(dataset)
    
    def predict(self, X):
        preditions = [self.make_prediction(x, self.root) for x in X]
        return preditions
    
    def make_prediction(self, x, tree):
        # be ezay feature ha baray yek seri nemone(test), ba estefade az derakht tasmim pishbini mikonad
        if tree.value!=None: return tree.value
        feature_val = x[tree.feature_idx]
        if feature_val<=tree.threshold:
            return self.make_prediction(x, tree.left)
        else:
            return self.make_prediction(x, tree.right)
''' **********************************************dade hay restaurant*******************************************************'''
#dade ha ro az file csv mikhanad 
col_names1 = ['Alt' ,'Bar'  , 'Fri', 'Hun', 'Pat', 'Price', 'Rain' , 'Res' , 'Type' , 'Est' , 'Goal']
data1 = pd.read_csv("resturant.csv", skiprows=1, header=None, names=col_names1)

# feature ha va outcome ro joda mikonad
X1 = data1.iloc[:, :-1].values
Y1 = data1.iloc[:, -1].values.reshape(-1,1)

# derakht ra misazad va an ra print mikonad
classifierR = DecisionTree(min_samples=2, max_depth=3)
classifierR.fit(X1,Y1)
print("             **tree of restaurant dataset**                ")
classifierR.print_tree(col_names1)
print("-"*160)



''' **********************************************dade hay diabete*******************************************************'''
#dade ha ro az file csv mikhanad 
col_names = ['Pregnancies' ,'Glucose'  , 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction' , 'Age' , 'Outcome']
data = pd.read_csv("diabetes.csv", skiprows=1, header=None, names=col_names)

# feature ha va outcome ro joda mikonad
X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values.reshape(-1,1)

# dade hay test va train ba nesbat 20 darsad dade test va 80 darsad dade train joda mikonad
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.2, random_state=41)

# derakht ra misazad va an ra print mikonad
classifier = DecisionTree(min_samples=2, max_depth=3)
classifier.fit(X_train,Y_train)
print("             **tree of diabete dataset**             ")
classifier.print_tree(col_names)

# be ezay dade test khoroji ra ba estefade az derakht sakhte shode emtehan mikonad
Y_pred = classifier.predict(X_test) 
# va sehat va dorosti an ra ba tavajo be on dataset diabete ke darim misanjad
acc = accuracy_score(Y_test, Y_pred)
print(f"with accuracy : {acc}")

