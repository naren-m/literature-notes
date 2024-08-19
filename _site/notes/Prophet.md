# Prophet

Prophet is a library for [[time series]] forecasting developed by Facebook. It's a robust, easy-to-use method that is particularly well-suited for forecasting time series with strong seasonal and trend components.


Prophet is based on decomposable time series models and it uses additive models where non-linear trends are fit with yearly and weekly seasonality, plus holidays. It can handle missing data, outliers, and large number of important events.

Prophet can be a good choice if your expenses data has strong seasonal and trend components, as it is designed to handle such cases. It can also handle missing data and outliers, which is a common problem in time series data.

However, it's important to note that, Prophet is not a one-size-fits-all solution, and it may not perform well on all types of data. It's always a good idea to try multiple algorithms and see which one works best for your dataset.

You can use the prophet package in Golang to use the Prophet algorithm, or you can use the python library and call it from your Go program using the [[gopy]] package.

```go
package main

import (
    "fmt"

    "github.com/facebook/prophet"
    "github.com/facebook/prophet/data"
    "github.com/facebook/prophet/filtering"
)

func prophetPredict(expenses []Expense) {
    // Prepare dataframe
    df := data.NewFrame("ds", "y")
    for _, expense := range expenses {
        df.AddRow(expense.Date, expense.Amount)
    }

    // Create a new prophet model
    model := prophet.New()
    model.Fit(df)

    // Create a new dataframe to hold the future data
    future := model.MakeFutureDataframe(365)

    // Predict future expenses
    forecast := model.Predict(future)

    fmt.Println(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]])
}

func main() {
    expenses := generateExpenses(365)
    prophetPredict(expenses)
}
```

