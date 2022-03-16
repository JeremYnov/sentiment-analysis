import textblob
import matplotlib.pyplot as plt


class SentimentAnalyzer:
    def analysis(self,df_to_analyze):
        df_to_analyze["Polarity"] = df_to_analyze["Text"].map(
            lambda text: textblob.TextBlob(text).sentiment.polarity
        )
        df_to_analyze["Result"] = df_to_analyze["Polarity"].map(
            lambda polarity: "+" if polarity > 0 else ("-" if polarity < 0 else "=")
        )
        self.barChartPreprocessing(df_to_analyze)
        self.barChart()

    def barChartPreprocessing(self, df_to_analyze):
        self.positives = df_to_analyze[df_to_analyze.Result == "+"].count()[
            "Text"
        ]
        self.negatives = df_to_analyze[df_to_analyze.Result == "-"].count()[
            "Text"
        ]
        self.neutrals = df_to_analyze[df_to_analyze.Result == "="].count()[
            "Text"
        ]
        print(
            f"Positive: {self.positives}, Negative: {self.negatives}, Neutral: {self.neutrals}"
        )

    def barChart(self):
        plt.bar(
            [0, 1, 2],
            [self.neutrals, self.positives, self.negatives],
            label=["Neutral", "Positive", "Negative"],
            color=["grey", "green", "red"],
        )
        plt.legend()
        plt.show()
        
    def analyzeByDate(self, df_to_analyze):
        print('test')
