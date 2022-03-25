def compute_mse(labels_tensor, prediction_tensor):
    mse_tensor = (labels_tensor - prediction_tensor)**2
    return mse_tensor