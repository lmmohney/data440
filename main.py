from src.data import make_data, save_data
from src.viz import make_figrue

def main():
    data=make_data
    save_data(data, 'test2.npy')
    make_figrue(data, 'test_figure.svg')


if __name__ == "__main__":
    main()
