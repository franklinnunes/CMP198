# Gene expression of non-small cell lung cancer (RNAseq) classification, biomarker identification using feature selection embedded tree-based model and interpretability
* this project was carried out as the final assignment for the course Algorithms for Bioinformatics and Computational Biology in the postgraduate course in computing at the federal university of rio grande do sul.

# Project Methodology
* the methodology used in the gene expression study of non-small cell lung cancer (NSCLC) to identify important genes and improve disease classification using machine learning.
  ![Screenshot(19)](https://github.com/user-attachments/assets/224568d8-0ea2-4725-883f-7feaaf7560c6)


## Data Acquisition
* Gene expression data from the GSE81089 dataset, available on Gene Expression Omnibus. This dataset includes tumor tissue samples from 199 NSCLC patients and 18 healthy lung tissue samples, collected during surgical procedures in Sweden between 2006 and 2010. RNA quality was verified, and RNAseq libraries were sequenced on the Illumina HiSeq 2500 platform.

## Data Preprocessing
* First, the data was normalized using MinMaxScaler to scale gene expression values to a binary range (0-1), ensuring all features contributed equally to the analysis. Subsequently, the dataset's dimensionality was reduced by 50% (from 39975 to 19987 features) using the SelectKBest method with the f_classif scoring function, selecting the most informative features.

## Machine Learning Approach
* Three tree-based machine learning models were employed: Decision Tree, Random Forest, and LightGBM. Hyperparameter optimization for each model was performed using Bayesian Optimization, an efficient probabilistic approach to find the best parameter combination.

## Cross-Validation
* Model performance was evaluated using leave-one-out cross-validation (LOOCV), where each sample served as a test case. Each model was fitted 11 times, and metrics such as accuracy, F1-score, precision, recall, ROC AUC, sensitivity, and specificity were calculated. The average of these metrics was used to determine the model with the best overall performance.

## Embedded Feature Selection and Interpretability
The best-performing model was then used for feature selection through an embedded method. The top 10 features identified by this model were reviewed in the literature to explore their relevance. Additionally, the dataset was split into 80% training and 20% testing subsets. For model interpretability, 40 tumor samples from the test set were analyzed using LIME, which illustrates each feature's contribution to these samples' predictions.

## Literature Review
* Official gene names corresponding to the 10 features selected by Random Forest (feature_importances_) and the LIME local explainer were retrieved from the Ensembl database. Protein products and biological functions were collected from UniProt (UniProt Consortium, 2023). A comprehensive literature review was conducted in major scientific databases like Scopus and PubMed to assess the association of the selected genes with cancer, using specific search terms.

## Libraries Used
### The proposed approach was implemented in Python 3. Key libraries used include:
* Scikit-Learn: For general machine learning tasks.
* LightGBM: For the implementation of the LightGBM model.
* Hyperopt: For model hyperparameter optimization.
* LIME: For explaining individual local model predictions.
