import csv
from .multilabel_classification import MultiLabelClassificationDataset

LABELS = ["haze", "primary", "agriculture", "clear", "water", "habitation", "road", "cultivation", "slash_burn",
          "cloudy", "partly_cloudy", "conventional_mine", "bare_ground", "artisinal_mine", "blooming",
          "selective_logging", "blow_down"]


class PlanetUASMultiLabelDataset(MultiLabelClassificationDataset):
    url = "https://www.kaggle.com/c/planet-understanding-the-amazon-from-space/overview"

    labels = LABELS
    name = "Planet UAS multilabel dataset"

    def __init__(self, config):
        # now call the constructor to validate the schema and load the data
        MultiLabelClassificationDataset.__init__(self, config)

    def __getitem__(self, index):
        """
        Args:
            index (int): Index

        Returns:
            tuple: (image, target) where target is index of the target class.
        """
        # load image
        img = self.image_loader(self.data[index][0])
        if self.transform:
            img = self.transform(img)
        target = self.data[index][1]
        if self.target_transform:
            target = self.target_transform(self.data[index][1])
        return img[:3], target


# Run this Function to convert the dataset in PASCAL VOC data format
def prepare(csv_train_file):
    f = open("multilabels.txt", "w")
    labels = []
    images = {}

    with open(csv_train_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                tmp_labels = row[1].split(' ')
                images[row[0]] = tmp_labels
                for label in tmp_labels:
                    if label not in labels:
                        labels.append(label)
                line_count += 1

    header = '\t'.join(labels)
    f.write("image\t" + header + "\n")

    for k, v in images.items():
        tmp_image = ""
        for label in labels:
            if label in v:
                tmp_image += "1\t"
            else:
                tmp_image += "0\t"
        f.write(k + "\t" + tmp_image[:-1] + "\n")
    f.close()
