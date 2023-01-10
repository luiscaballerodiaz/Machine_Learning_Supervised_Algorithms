from datacsv import DataBinaryOutputCSV


datacsv = DataBinaryOutputCSV('cardio_train.csv')
sourcedf = datacsv.read_csv()
datacsv.binary_class_histogram(dataset=sourcedf, class_column_name='cardio', plot_name='Original histogram.png',
                               x_axes_name='Feature magnitude', y_axes_name='Frequency')
df = datacsv.data_scrubbing(dataset=sourcedf, columns_to_remove='id', concept1='ap_lo', concept2='ap_hi',
                            encodings=['gender', 'cholesterol', 'gluc'], class_column_name='cardio')
datacsv.binary_class_histogram(dataset=df, class_column_name='cardio', plot_name='Scrubber histogram.png',
                               x_axes_name='Feature magnitude', y_axes_name='Frequency')
datacsv.train_test_split(feature_data=df.iloc[:, :-1], class_data=df.iloc[:, [-1]], test_size=0.2)
datacsv.data_scaling(algorithm='standard')
datacsv.apply_pca(ncomps=df.shape[1]-1)

datacsv.apply_algorithm(algorithm='knn', params={'n_neighbors': 2})
datacsv.apply_algorithm(algorithm='knn', params={'n_neighbors': 7})
datacsv.apply_algorithm(algorithm='knn', params={'n_neighbors': 25})
datacsv.apply_algorithm(algorithm='linearsvc', params={'C': 0.01})
datacsv.apply_algorithm(algorithm='linearsvc', params={'C': 1000})
datacsv.apply_algorithm(algorithm='logreg', params={'C': 0.01})
datacsv.apply_algorithm(algorithm='logreg', params={'C': 1000})
datacsv.apply_algorithm(algorithm='naivebayes', params={})
datacsv.apply_algorithm(algorithm='tree', params={'max_depth': 25})
datacsv.apply_algorithm(algorithm='tree', params={'max_depth': 5})
datacsv.apply_algorithm(algorithm='forest', params={'n_estimators': 5, 'max_features': 11, 'max_depth': 25})
datacsv.apply_algorithm(algorithm='forest', params={'n_estimators': 5, 'max_features': 4, 'max_depth': 25})
datacsv.apply_algorithm(algorithm='forest', params={'n_estimators': 100, 'max_features': 4, 'max_depth': 25})
datacsv.apply_algorithm(algorithm='forest', params={'n_estimators': 100, 'max_features': 4, 'max_depth': 8})
datacsv.apply_algorithm(algorithm='forest', params={'n_estimators': 200, 'max_features': 4, 'max_depth': 8})
datacsv.apply_algorithm(algorithm='gradient', params={'n_estimators': 500, 'learning_rate': 1, 'max_depth': 4})
datacsv.apply_algorithm(algorithm='gradient', params={'n_estimators': 25, 'learning_rate': 1, 'max_depth': 4})
datacsv.apply_algorithm(algorithm='gradient', params={'n_estimators': 25, 'learning_rate': 0.2, 'max_depth': 4})
datacsv.apply_algorithm(algorithm='mlp', params={'activation': 'tanh', 'alpha': 0.01, 'hidden_layer_sizes': [50, 50]})
datacsv.apply_algorithm(algorithm='mlp', params={'activation': 'tanh', 'alpha': 0.01, 'hidden_layer_sizes': 100})
datacsv.apply_algorithm(algorithm='mlp', params={'activation': 'tanh', 'alpha': 10, 'hidden_layer_sizes': 100})
datacsv.apply_algorithm(algorithm='svm', params={'kernel': 'rbf', 'C': 0.1, 'gamma': 1})
datacsv.write_results_excel_file('results.xlsx')
