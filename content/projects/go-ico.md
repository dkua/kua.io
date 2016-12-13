+++
title = "go-ico"
date = "2016-12-13T01:49:02-05:00"
slug = "go-ico"
+++

``` go
package main

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBB

import "fmt"

func ComputeAValue(c chan<- float64) {
    // Do the computation.
    c <- 2.3423 / 534.23423
}

func UseAGoroutine() float64 {
channel := make(chan float64) go ComputeAValue(channel) // do something else for a while areturn <- channel
}

func main() {
value := UseAGoroutine()
           fmt.Printf("Result was: %v", value)
}
```

