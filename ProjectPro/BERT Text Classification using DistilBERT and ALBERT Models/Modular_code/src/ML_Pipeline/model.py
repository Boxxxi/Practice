import ktrain
import timeit
from ktrain import text


def create_and_train_model(train, val, transformer_model, model_name):
    model = transformer_model.get_classifier()
    model_learner_ins = None
    if model_name == "albert":
        print("\nCompiling & Training ALBERT for maxlen=512 & batch_size=6")
        model_learner_ins = ktrain.get_learner(model=model,
                                               train_data=train,
                                               val_data=val,
                                               batch_size=6)

        print("Transformer Layers: \n", model_learner_ins.layers)
        print("Model Summary: \n", model_learner_ins.model.summary())
        start_time = timeit.default_timer()
        print("\nFine Tuning ALBERT on Dbpedia Dataset with learning rate=2e-5 and epochs=1")
        model_learner_ins.fit_onecycle(lr=2e-5, epochs=1)
        stop_time = timeit.default_timer()
        print("Total time in minutes for Fine-Tuning ALBERT on Dbpedia Dataset: \n", (stop_time - start_time) / 60)

    elif model_name == "distilbert":
        print("\nCompiling & Training DistilBERT for maxlen=512 & batch_size=16")
        model_learner_ins = ktrain.get_learner(model=model,
                                               train_data=train,
                                               val_data=val,
                                               batch_size=16)

        print("Transformer Layers: \n", model_learner_ins.layers)
        print("Model Summary: \n", model_learner_ins.model.summary())
        start_time = timeit.default_timer()
        print("\nFine Tuning DistilBERT on Dbpedia Dataset with learning rate=2e-5 and epochs=1")
        model_learner_ins.fit_onecycle(lr=2e-5, epochs=1)
        stop_time = timeit.default_timer()
        print("Total time in minutes for Fine-Tuning DistilBERT on Dbpedia Dataset: \n", (stop_time - start_time) / 60)

    return model_learner_ins


def check_model_performance(model_learner_ins, class_label_names, model_name):
    print("{} Performance Metrics on Dbpedia Dataset :\n".format(model_name), model_learner_ins.validate())
    print("{} Performance Metrics on Dbpedia Dataset with Class Names :\n".format(model_name),
          model_learner_ins.validate(class_names=class_label_names))
    return None


def save_fine_tuned_model(model_learner_ins, preprocessing_var, model_name):
    if model_name == "albert":
        predictor = ktrain.get_predictor(model_learner_ins.model, preproc=preprocessing_var)
        predictor.save('../output/albert-content/albert-predictor-on-dbpedia')
    elif model_name == "distilbert":
        predictor = ktrain.get_predictor(model_learner_ins.model, preproc=preprocessing_var)
        predictor.save('../output/distilbert-content/distilbert-predictor-on-dbpedia')
    return None

