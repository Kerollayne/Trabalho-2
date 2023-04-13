import matplotlib.pyplot as plt
from sklearn import metrics

def plot_roc_curve(label, calcClass):
    fpr, tpr, thresholds = metrics.roc_curve(label, calcClass, pos_label=2)
    roc_auc = metrics.auc(fpr, tpr)

    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.axis([0, 1, 0, 1])  # Define os limites dos eixos
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic')
    plt.legend(loc="lower right")

    plt.show()
