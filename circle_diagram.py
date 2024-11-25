import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def create_dataframe_from_csv() -> pd.DataFrame:
    data_set_file = 'Electric_Car (1).csv'
    dataframe = pd.read_csv(data_set_file)
    return dataframe



if __name__ == '__main__':
    df = create_dataframe_from_csv()
    df = df.sort_values('TopSpeed_KmH', ascending=True)
    df = df['Brand'].value_counts()

    data_array = np.array(df)

    # Находим топ-5 значений
    top_5_brands = np.sort(data_array)[-5:]


    # Находим сумму оставшихся значений
    other_sum = np.sum(data_array) - np.sum(top_5_brands)

    # Создаём массив значений для круговой диаграммы
    plot_values = np.append(top_5_brands, other_sum)

    # Подписываем сектора
    plot_labels = [df.index[i] for i in range(5)] + ['Others']

    # Строим круговую диаграмму
    plt.figure(figsize=(8, 8))
    plt.pie(plot_values, labels=plot_labels, autopct='%1.1f%%', startangle=90)
    plt.title('Круговая диаграмма с 6 секторами')
    plt.show()



