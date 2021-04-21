import fire
import pickle 
import logging
import pandas

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Classifier:
    """
    Train or predict from dataset
    """
    def predict(self, predict_data_path: str, output_path: str):
        model_path = 'mask_rcnn/test_images.py'
        """
        Predicts `predict_data_path` data using `model_path` 
        model and saves predictions to         `output_path`
        :param predict_data_path: path to data for predictions
        :param model_path: path to trained model
        :param output_path: path to save predictions
        """
        logger.info(f"Loading data for predictions from {predict_data_path} ...")
        #X = pandas.read_csv(predict_data_path)

        logger.info(f"Loading model from {model_path} ...")
        #model = load_model(model_path)

        logger.info("Running model predictions...")
        #y_pred = model.predict(X)

        logger.info(f"Saving predictions to {output_path} ...")
        #pandas.DataFrame(y_pred).to_csv(output_path)

        

        logger.info("Successfully predicted.")

if __name__ == "__main__":
    fire.Fire(Classifier)
