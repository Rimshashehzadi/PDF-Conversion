import pandas as pd #type: ignore

# Sample JSON data
data = {
  "document": {
    "@pageCount": "2",
    "@pageCountWithOCRPerformed": "0",
    "page": [
      {
        "@index": "0",
        "@width": "596",
        "@height": "842",
        "@OCRWasPerformed": "False",
        "row": [
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Times",
                  "@fontSize": "33.0",
                  "@x": "139.71",
                  "@y": "57.24",
                  "@width": "314.76",
                  "@height": "33.24",
                  "#text": "NEW BEST PRICE LIST"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "54.24",
                  "@y": "122.12",
                  "@width": "68.40",
                  "@height": "11.05",
                  "#text": "Unique Model"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "26.64",
                  "@y": "129.11",
                  "@width": "17.19",
                  "@height": "11.05",
                  "#text": "No."
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "138.47",
                  "@y": "129.11",
                  "@width": "78.10",
                  "@height": "11.05",
                  "#text": "Product's Name"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "257.06",
                  "@y": "129.11",
                  "@width": "28.82",
                  "@height": "11.05",
                  "#text": "Photo"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "349.95",
                  "@y": "129.11",
                  "@width": "63.26",
                  "@height": "11.05",
                  "#text": "Specification"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "75.35",
                  "@y": "136.06",
                  "@width": "26.42",
                  "@height": "11.05",
                  "#text": "Code"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Times",
                  "@fontSize": "15.0",
                  "@x": "470.43",
                  "@y": "148.65",
                  "@width": "22.40",
                  "@height": "14.79",
                  "#text": "MOQ"
                }
              },
              {
                "text": {
                  "@fontName": "Times",
                  "@fontSize": "15.0",
                  "@x": "533.32",
                  "@y": "148.65",
                  "@width": "22.38",
                  "@height": "14.79",
                  "#text": "USD"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "172.41",
                  "@width": "114.62",
                  "@height": "9.25",
                  "#text": "Dimension:800*900*920mm"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "144.27",
                  "@y": "183.81",
                  "@width": "66.59",
                  "@height": "11.05",
                  "#text": "4-Burner Gas"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "183.96",
                  "@width": "22.54",
                  "@height": "9.25",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "32.16",
                  "@y": "197.75",
                  "@width": "6.15",
                  "@height": "11.05",
                  "#text": "1"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "65.05",
                  "@y": "197.75",
                  "@width": "46.80",
                  "@height": "11.05",
                  "#text": "HGR-905"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "136.31",
                  "@y": "197.75",
                  "@width": "82.26",
                  "@height": "11.05",
                  "#text": "Range With Gas"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "195.23",
                  "@width": "119.03",
                  "@height": "9.25",
                  "#text": "Dimensions:550*680*270mm"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "478.11",
                  "@y": "196.36",
                  "@width": "7.17",
                  "@height": "12.90",
                  "#text": "5"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "525.17",
                  "@y": "196.36",
                  "@width": "39.05",
                  "@height": "12.90",
                  "#text": "$577.5"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "206.73",
                  "@width": "111.27",
                  "@height": "9.25",
                  "#text": "LPG2800-3700Pa:2.62kg/h"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "164.18",
                  "@y": "211.69",
                  "@width": "26.41",
                  "@height": "11.05",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "218.28",
                  "@width": "111.57",
                  "@height": "9.25",
                  "#text": "NG2000-2500Pa:3.70m3/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "229.78",
                  "@width": "125.85",
                  "@height": "9.25",
                  "#text": "Power Supply:7 5 x 4 + 5 8KW"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "236.49",
                  "@width": "114.62",
                  "@height": "9.25",
                  "#text": "Dimension:800*900*920mm"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "144.27",
                  "@y": "247.89",
                  "@width": "66.59",
                  "@height": "11.05",
                  "#text": "4-Burner Gas"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "248.04",
                  "@width": "22.54",
                  "@height": "9.25",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "32.16",
                  "@y": "261.83",
                  "@width": "6.15",
                  "@height": "11.05",
                  "#text": "2"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "61.46",
                  "@y": "261.83",
                  "@width": "54.14",
                  "@height": "11.05",
                  "#text": "HGR-905A"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "128.16",
                  "@y": "261.83",
                  "@width": "98.59",
                  "@height": "11.05",
                  "#text": "Range With Electric"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "259.31",
                  "@width": "119.03",
                  "@height": "9.25",
                  "#text": "Dimensions:550*680*270mm"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "478.11",
                  "@y": "260.44",
                  "@width": "7.17",
                  "@height": "12.90",
                  "#text": "5"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "525.17",
                  "@y": "260.44",
                  "@width": "39.05",
                  "@height": "12.90",
                  "#text": "$549.3"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "270.81",
                  "@width": "111.27",
                  "@height": "9.25",
                  "#text": "LPG2800-3700Pa:2.62kg/h"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "164.18",
                  "@y": "275.77",
                  "@width": "26.41",
                  "@height": "11.05",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "282.36",
                  "@width": "111.57",
                  "@height": "9.25",
                  "#text": "NG2000-2500Pa:3.70m3/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "293.86",
                  "@width": "125.85",
                  "@height": "9.25",
                  "#text": "Power Supply:7 5 x 4 + 5 8KW"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "300.58",
                  "@width": "114.62",
                  "@height": "9.25",
                  "#text": "Dimension:700*700*920mm"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "144.27",
                  "@y": "311.98",
                  "@width": "66.59",
                  "@height": "11.05",
                  "#text": "4-Burner Gas"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "312.12",
                  "@width": "22.54",
                  "@height": "9.25",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "32.16",
                  "@y": "325.92",
                  "@width": "6.15",
                  "@height": "11.05",
                  "#text": "3"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "65.05",
                  "@y": "325.92",
                  "@width": "46.80",
                  "@height": "11.05",
                  "#text": "HGR-705"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "136.31",
                  "@y": "325.92",
                  "@width": "82.26",
                  "@height": "11.05",
                  "#text": "Range With Gas"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "323.39",
                  "@width": "119.03",
                  "@height": "9.25",
                  "#text": "Dimensions:550*550*270mm"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "478.11",
                  "@y": "324.53",
                  "@width": "7.17",
                  "@height": "12.90",
                  "#text": "5"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "525.17",
                  "@y": "324.53",
                  "@width": "39.05",
                  "@height": "12.90",
                  "#text": "$549.3"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "334.94",
                  "@width": "112.80",
                  "@height": "9.25",
                  "#text": "LPG2800-3700Pa:2.06kg/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "164.18",
                  "@y": "339.85",
                  "@width": "26.41",
                  "@height": "11.05",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "346.44",
                  "@width": "111.57",
                  "@height": "9.25",
                  "#text": "NG2000-2500Pa:3.07m3/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "357.94",
                  "@width": "125.85",
                  "@height": "9.25",
                  "#text": "Power Supply:7 5 x 4 + 5 8KW"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "364.66",
                  "@width": "114.62",
                  "@height": "9.25",
                  "#text": "Dimension:700*700*920mm"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "144.27",
                  "@y": "376.06",
                  "@width": "66.59",
                  "@height": "11.05",
                  "#text": "4-Burner Gas"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "376.21",
                  "@width": "22.54",
                  "@height": "9.25",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "32.16",
                  "@y": "390.00",
                  "@width": "6.15",
                  "@height": "11.05",
                  "#text": "4"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "61.46",
                  "@y": "390.00",
                  "@width": "54.14",
                  "@height": "11.05",
                  "#text": "HGR-705A"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "128.16",
                  "@y": "390.00",
                  "@width": "98.59",
                  "@height": "11.05",
                  "#text": "Range With Electric"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "387.48",
                  "@width": "119.03",
                  "@height": "9.25",
                  "#text": "Dimensions:550*550*270mm"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "478.11",
                  "@y": "388.61",
                  "@width": "7.17",
                  "@height": "12.90",
                  "#text": "5"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "525.17",
                  "@y": "388.61",
                  "@width": "39.05",
                  "@height": "12.90",
                  "#text": "$521.1"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "399.02",
                  "@width": "112.80",
                  "@height": "9.25",
                  "#text": "LPG2800-3700Pa:2.06kg/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "164.18",
                  "@y": "403.94",
                  "@width": "26.41",
                  "@height": "11.05",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "410.52",
                  "@width": "111.57",
                  "@height": "9.25",
                  "#text": "NG2000-2500Pa:3.07m3/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "422.02",
                  "@width": "125.85",
                  "@height": "9.25",
                  "#text": "Power Supply:7 5 x 4 + 5 8KW"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "437.90",
                  "@width": "114.62",
                  "@height": "9.25",
                  "#text": "Dimesnion:800*900*920mm"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "144.27",
                  "@y": "447.13",
                  "@width": "66.34",
                  "@height": "11.05",
                  "#text": "Gas 4-Burner"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "449.40",
                  "@width": "114.32",
                  "@height": "9.25",
                  "#text": "LPG2800-3700Pa:2.06Kg/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "32.16",
                  "@y": "454.08",
                  "@width": "6.15",
                  "@height": "11.05",
                  "#text": "5"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "61.46",
                  "@y": "454.08",
                  "@width": "54.14",
                  "@height": "11.05",
                  "#text": "HGR-905B"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "460.94",
                  "@width": "111.57",
                  "@height": "9.25",
                  "#text": "NG2000-2500Pa:3.07m3/H"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "478.11",
                  "@y": "452.74",
                  "@width": "7.17",
                  "@height": "12.90",
                  "#text": "5"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "525.17",
                  "@y": "452.74",
                  "@width": "39.05",
                  "@height": "12.90",
                  "#text": "$436.6"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "129.13",
                  "@y": "461.03",
                  "@width": "96.68",
                  "@height": "11.05",
                  "#text": "Range with Cabinet"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "472.44",
                  "@width": "102.30",
                  "@height": "9.25",
                  "#text": "Power Supply:7.5 x 4KW"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "501.98",
                  "@width": "114.62",
                  "@height": "9.25",
                  "#text": "Dimesnion:700*700*920mm"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "144.27",
                  "@y": "511.22",
                  "@width": "66.34",
                  "@height": "11.05",
                  "#text": "Gas 4-Burner"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "513.48",
                  "@width": "114.32",
                  "@height": "9.25",
                  "#text": "LPG2800-3700Pa:2.06Kg/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "32.16",
                  "@y": "518.16",
                  "@width": "6.15",
                  "@height": "11.05",
                  "#text": "6"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "61.46",
                  "@y": "518.16",
                  "@width": "54.14",
                  "@height": "11.05",
                  "#text": "HGR-705B"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "525.03",
                  "@width": "111.57",
                  "@height": "9.25",
                  "#text": "NG2000-2500Pa:3.07m3/H"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "478.11",
                  "@y": "516.82",
                  "@width": "7.17",
                  "@height": "12.90",
                  "#text": "5"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "525.17",
                  "@y": "516.82",
                  "@width": "39.05",
                  "@height": "12.90",
                  "#text": "$408.5"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "129.13",
                  "@y": "525.11",
                  "@width": "96.68",
                  "@height": "11.05",
                  "#text": "Range with Cabinet"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "536.53",
                  "@width": "102.30",
                  "@height": "9.25",
                  "#text": "Power Supply:7.5 x 4KW"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "556.95",
                  "@width": "114.62",
                  "@height": "9.25",
                  "#text": "Dimension:800*900*920mm"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "144.27",
                  "@y": "568.35",
                  "@width": "66.34",
                  "@height": "11.05",
                  "#text": "Gas 4-Burner"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "568.45",
                  "@width": "22.54",
                  "@height": "9.25",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "32.16",
                  "@y": "582.25",
                  "@width": "6.15",
                  "@height": "11.05",
                  "#text": "7"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "66.48",
                  "@y": "582.25",
                  "@width": "44.17",
                  "@height": "11.05",
                  "#text": "HX-905Z"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "138.01",
                  "@y": "582.25",
                  "@width": "78.83",
                  "@height": "11.05",
                  "#text": "Range with Gas"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "579.72",
                  "@width": "114.62",
                  "@height": "9.25",
                  "#text": "Dimension:550*680*270mm"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "478.11",
                  "@y": "580.90",
                  "@width": "7.17",
                  "@height": "12.90",
                  "#text": "5"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "525.17",
                  "@y": "580.90",
                  "@width": "39.05",
                  "@height": "12.90",
                  "#text": "$612.7"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "591.27",
                  "@width": "112.80",
                  "@height": "9.25",
                  "#text": "LPG2800-3700Pa:2.10kg/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "164.18",
                  "@y": "596.18",
                  "@width": "26.41",
                  "@height": "11.05",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "602.77",
                  "@width": "118.36",
                  "@height": "9.25",
                  "#text": "NG2000-2500Pa：2.81m3/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "614.32",
                  "@width": "25.76",
                  "@height": "9.25",
                  "#text": "Power"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "621.03",
                  "@width": "114.62",
                  "@height": "9.25",
                  "#text": "Dimension:800*900*920mm"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "144.27",
                  "@y": "632.43",
                  "@width": "66.34",
                  "@height": "11.05",
                  "#text": "Gas 4-Burner"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "632.54",
                  "@width": "22.54",
                  "@height": "9.25",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "32.16",
                  "@y": "646.33",
                  "@width": "6.15",
                  "@height": "11.05",
                  "#text": "8"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "62.65",
                  "@y": "646.33",
                  "@width": "51.91",
                  "@height": "11.05",
                  "#text": "HX-905ZA"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "129.87",
                  "@y": "646.33",
                  "@width": "95.23",
                  "@height": "11.05",
                  "#text": "Range with Electric"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "643.81",
                  "@width": "114.62",
                  "@height": "9.25",
                  "#text": "Dimension:550*680*270mm"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "478.11",
                  "@y": "644.98",
                  "@width": "7.17",
                  "@height": "12.90",
                  "#text": "5"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "525.17",
                  "@y": "644.98",
                  "@width": "39.05",
                  "@height": "12.90",
                  "#text": "$577.5"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "655.35",
                  "@width": "112.80",
                  "@height": "9.25",
                  "#text": "LPG2800-3700Pa:2.10kg/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "164.18",
                  "@y": "660.27",
                  "@width": "26.41",
                  "@height": "11.05",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "666.85",
                  "@width": "118.36",
                  "@height": "9.25",
                  "#text": "NG2000-2500Pa：2.81m3/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "678.40",
                  "@width": "25.76",
                  "@height": "9.25",
                  "#text": "Power"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "694.23",
                  "@width": "114.62",
                  "@height": "9.25",
                  "#text": "Dimension:800*900*920mm"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "144.27",
                  "@y": "703.46",
                  "@width": "66.34",
                  "@height": "11.05",
                  "#text": "Gas 4-Burner"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "705.73",
                  "@width": "112.80",
                  "@height": "9.25",
                  "#text": "LPG2800-3700Pa:1.73kg/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "32.16",
                  "@y": "710.41",
                  "@width": "6.15",
                  "@height": "11.05",
                  "#text": "9"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "58.10",
                  "@y": "710.41",
                  "@width": "61.01",
                  "@height": "11.05",
                  "#text": "HGR-905ZB"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "478.11",
                  "@y": "709.07",
                  "@width": "7.17",
                  "@height": "12.90",
                  "#text": "5"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "525.17",
                  "@y": "709.07",
                  "@width": "39.05",
                  "@height": "12.90",
                  "#text": "$471.8"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "129.13",
                  "@y": "717.40",
                  "@width": "96.68",
                  "@height": "11.05",
                  "#text": "Range with Cabinet"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "717.27",
                  "@width": "110.03",
                  "@height": "9.25",
                  "#text": "NG2000-2500Pa:2.33m3/h"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "728.77",
                  "@width": "125.07",
                  "@height": "9.25",
                  "#text": "Power Supply:7.5x2+4.5x2KW"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          }
        ]
      },
      {
        "@index": "1",
        "@width": "596",
        "@height": "842",
        "@OCRWasPerformed": "False",
        "row": [
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "54.24",
                  "@y": "76.76",
                  "@width": "68.40",
                  "@height": "11.05",
                  "#text": "Unique Model"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "26.64",
                  "@y": "83.48",
                  "@width": "17.19",
                  "@height": "11.05",
                  "#text": "No."
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "138.47",
                  "@y": "83.48",
                  "@width": "78.10",
                  "@height": "11.05",
                  "#text": "Product's Name"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "257.06",
                  "@y": "83.48",
                  "@width": "28.82",
                  "@height": "11.05",
                  "#text": "Photo"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "349.95",
                  "@y": "83.48",
                  "@width": "63.26",
                  "@height": "11.05",
                  "#text": "Specification"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "75.35",
                  "@y": "90.47",
                  "@width": "26.42",
                  "@height": "11.05",
                  "#text": "Code"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Times",
                  "@fontSize": "15.0",
                  "@x": "470.43",
                  "@y": "103.06",
                  "@width": "22.40",
                  "@height": "14.79",
                  "#text": "MOQ"
                }
              },
              {
                "text": {
                  "@fontName": "Times",
                  "@fontSize": "15.0",
                  "@x": "533.32",
                  "@y": "103.06",
                  "@width": "22.38",
                  "@height": "14.79",
                  "#text": "USD"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "126.82",
                  "@width": "119.68",
                  "@height": "9.25",
                  "#text": "Dimension:1200*900*920mm"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "144.26",
                  "@y": "138.22",
                  "@width": "66.34",
                  "@height": "11.05",
                  "#text": "Gas 6-Burner"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "138.32",
                  "@width": "22.54",
                  "@height": "9.25",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "29.03",
                  "@y": "152.16",
                  "@width": "12.29",
                  "@height": "11.05",
                  "#text": "10"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "65.05",
                  "@y": "152.16",
                  "@width": "46.80",
                  "@height": "11.05",
                  "#text": "HGR-996"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "136.31",
                  "@y": "152.16",
                  "@width": "82.26",
                  "@height": "11.05",
                  "#text": "Range With Gas"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "149.64",
                  "@width": "114.62",
                  "@height": "9.25",
                  "#text": "Dimension:550*680*270mm"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "478.11",
                  "@y": "150.77",
                  "@width": "7.17",
                  "@height": "12.90",
                  "#text": "5"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "525.17",
                  "@y": "150.77",
                  "@width": "39.05",
                  "@height": "12.90",
                  "#text": "$725.4"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "161.14",
                  "@width": "114.32",
                  "@height": "9.25",
                  "#text": "LPG2800-3700Pa:3.55Kg/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "164.18",
                  "@y": "166.05",
                  "@width": "26.41",
                  "@height": "11.05",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "172.69",
                  "@width": "111.57",
                  "@height": "9.25",
                  "#text": "NG2000-2500Pa:5.26m3/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "183.96",
                  "@width": "115.13",
                  "@height": "9.25",
                  "#text": "Power Supply:7 5x6+5 8KW"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "190.90",
                  "@width": "119.68",
                  "@height": "9.25",
                  "#text": "Dimension:1050*700*920mm"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "144.26",
                  "@y": "202.30",
                  "@width": "66.34",
                  "@height": "11.05",
                  "#text": "Gas 6-Burner"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "202.45",
                  "@width": "22.54",
                  "@height": "9.25",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "29.03",
                  "@y": "216.24",
                  "@width": "12.29",
                  "@height": "11.05",
                  "#text": "11"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "65.05",
                  "@y": "216.24",
                  "@width": "46.80",
                  "@height": "11.05",
                  "#text": "HGR-776"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "136.31",
                  "@y": "216.24",
                  "@width": "82.26",
                  "@height": "11.05",
                  "#text": "Range With Gas"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "213.72",
                  "@width": "114.62",
                  "@height": "9.25",
                  "#text": "Dimension:560*600*270mm"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "478.11",
                  "@y": "214.85",
                  "@width": "7.17",
                  "@height": "12.90",
                  "#text": "5"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "525.17",
                  "@y": "214.85",
                  "@width": "39.05",
                  "@height": "12.90",
                  "#text": "$697.2"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "225.22",
                  "@width": "115.52",
                  "@height": "9.25",
                  "#text": "LPG2800-3700Pa:3.55 kg/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "164.18",
                  "@y": "230.14",
                  "@width": "26.41",
                  "@height": "11.05",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "236.77",
                  "@width": "111.57",
                  "@height": "9.25",
                  "#text": "NG2000-2500Pa:5.26m3/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "248.04",
                  "@width": "115.13",
                  "@height": "9.25",
                  "#text": "Power Supply:7 5x6+5 8KW"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "254.99",
                  "@width": "119.68",
                  "@height": "9.25",
                  "#text": "Dimension:1200*900*920mm"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "144.26",
                  "@y": "266.39",
                  "@width": "66.34",
                  "@height": "11.05",
                  "#text": "Gas 6-Burner"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "266.53",
                  "@width": "22.54",
                  "@height": "9.25",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "29.03",
                  "@y": "280.33",
                  "@width": "12.29",
                  "@height": "11.05",
                  "#text": "12"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "61.46",
                  "@y": "280.33",
                  "@width": "54.14",
                  "@height": "11.05",
                  "#text": "HGR-996A"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "128.16",
                  "@y": "280.33",
                  "@width": "98.59",
                  "@height": "11.05",
                  "#text": "Range With Electric"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "277.80",
                  "@width": "114.62",
                  "@height": "9.25",
                  "#text": "Dimension:550*680*270mm"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "478.11",
                  "@y": "278.94",
                  "@width": "7.17",
                  "@height": "12.90",
                  "#text": "5"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "525.17",
                  "@y": "278.94",
                  "@width": "39.05",
                  "@height": "12.90",
                  "#text": "$683.1"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "289.31",
                  "@width": "114.32",
                  "@height": "9.25",
                  "#text": "LPG2800-3700Pa:3.34Kg/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "164.18",
                  "@y": "294.22",
                  "@width": "26.41",
                  "@height": "11.05",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "300.85",
                  "@width": "111.57",
                  "@height": "9.25",
                  "#text": "NG2000-2500Pa:4.85m3/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "312.12",
                  "@width": "115.13",
                  "@height": "9.25",
                  "#text": "Power Supply:7 5x6+4 8KW"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "144.26",
                  "@y": "330.47",
                  "@width": "66.34",
                  "@height": "11.05",
                  "#text": "Gas 6-Burner"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "328.18",
                  "@width": "119.68",
                  "@height": "9.25",
                  "#text": "Dimension:1050*700*920mm"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "339.73",
                  "@width": "22.54",
                  "@height": "9.25",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "29.03",
                  "@y": "344.41",
                  "@width": "12.29",
                  "@height": "11.05",
                  "#text": "13"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "61.46",
                  "@y": "344.41",
                  "@width": "54.14",
                  "@height": "11.05",
                  "#text": "HGR-776A"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "128.16",
                  "@y": "344.41",
                  "@width": "98.59",
                  "@height": "11.05",
                  "#text": "Range With Electric"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "351.23",
                  "@width": "114.62",
                  "@height": "9.25",
                  "#text": "Dimension:550*550*270mm"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "478.11",
                  "@y": "343.02",
                  "@width": "7.17",
                  "@height": "12.90",
                  "#text": "5"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "525.17",
                  "@y": "343.02",
                  "@width": "39.05",
                  "@height": "12.90",
                  "#text": "$654.9"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "164.18",
                  "@y": "358.30",
                  "@width": "26.41",
                  "@height": "11.05",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "362.54",
                  "@width": "115.13",
                  "@height": "9.25",
                  "#text": "Power Supply:7.5x6+4.8KW"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "392.26",
                  "@width": "119.68",
                  "@height": "9.25",
                  "#text": "Dimension:1200*900*920mm"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "144.26",
                  "@y": "401.50",
                  "@width": "66.34",
                  "@height": "11.05",
                  "#text": "Gas 6-Burner"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "403.81",
                  "@width": "130.88",
                  "@height": "9.25",
                  "#text": "LPG 2800-3700Pa:3.34/2.4kg/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "29.03",
                  "@y": "408.49",
                  "@width": "12.29",
                  "@height": "11.05",
                  "#text": "14"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "61.46",
                  "@y": "408.49",
                  "@width": "54.14",
                  "@height": "11.05",
                  "#text": "HGR-996B"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "478.11",
                  "@y": "407.10",
                  "@width": "7.17",
                  "@height": "12.90",
                  "#text": "5"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "525.17",
                  "@y": "407.10",
                  "@width": "39.05",
                  "@height": "12.90",
                  "#text": "$549.3"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "129.13",
                  "@y": "415.44",
                  "@width": "96.68",
                  "@height": "11.05",
                  "#text": "Range with Cabinet"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "415.31",
                  "@width": "132.09",
                  "@height": "9.25",
                  "#text": "NG2000-2500Pa:4.66/3.49m3/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "426.63",
                  "@width": "125.07",
                  "@height": "9.25",
                  "#text": "Power Supply:7.5x3+4.5x3KW"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "144.26",
                  "@y": "458.63",
                  "@width": "66.34",
                  "@height": "11.05",
                  "#text": "Gas 6-Burner"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "456.39",
                  "@width": "119.68",
                  "@height": "9.25",
                  "#text": "Dimension:1200*900*920mm"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "467.89",
                  "@width": "130.88",
                  "@height": "9.25",
                  "#text": "LPG 2800-3700Pa:3.34/2.4kg/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "29.03",
                  "@y": "472.57",
                  "@width": "12.29",
                  "@height": "11.05",
                  "#text": "15"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "58.10",
                  "@y": "472.57",
                  "@width": "61.01",
                  "@height": "11.05",
                  "#text": "HGR-996ZB"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "129.13",
                  "@y": "472.57",
                  "@width": "96.68",
                  "@height": "11.05",
                  "#text": "Range with Cabinet"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "479.39",
                  "@width": "132.09",
                  "@height": "9.25",
                  "#text": "NG2000-2500Pa:4.66/3.49m3/H"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "478.11",
                  "@y": "471.18",
                  "@width": "7.17",
                  "@height": "12.90",
                  "#text": "5"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "525.17",
                  "@y": "471.18",
                  "@width": "39.05",
                  "@height": "12.90",
                  "#text": "$605.6"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "140.40",
                  "@y": "486.47",
                  "@width": "74.07",
                  "@height": "11.05",
                  "#text": "( Silver burner)"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "490.71",
                  "@width": "125.07",
                  "@height": "9.25",
                  "#text": "Power Supply:7.5x3+4.5x3KW"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "520.47",
                  "@width": "119.68",
                  "@height": "9.25",
                  "#text": "Dimension:1050*700*920mm"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "144.26",
                  "@y": "529.71",
                  "@width": "66.34",
                  "@height": "11.05",
                  "#text": "Gas 6-Burner"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "531.97",
                  "@width": "115.43",
                  "@height": "9.25",
                  "#text": "LPG 2800-3700Pa:3.34kg/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "29.03",
                  "@y": "536.66",
                  "@width": "12.29",
                  "@height": "11.05",
                  "#text": "16"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "61.46",
                  "@y": "536.66",
                  "@width": "54.14",
                  "@height": "11.05",
                  "#text": "HGR-776B"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "478.11",
                  "@y": "535.27",
                  "@width": "7.17",
                  "@height": "12.90",
                  "#text": "5"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "525.17",
                  "@y": "535.27",
                  "@width": "39.05",
                  "@height": "12.90",
                  "#text": "$507.0"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "129.13",
                  "@y": "543.60",
                  "@width": "96.68",
                  "@height": "11.05",
                  "#text": "Range with Cabinet"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "543.47",
                  "@width": "111.57",
                  "@height": "9.25",
                  "#text": "NG2000-2500Pa:4.66m3/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "554.79",
                  "@width": "102.30",
                  "@height": "9.25",
                  "#text": "Power Supply:7.5 x 6KW"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "575.40",
                  "@width": "119.68",
                  "@height": "9.25",
                  "#text": "Dimension:1200*900*920mm"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "144.26",
                  "@y": "586.80",
                  "@width": "66.34",
                  "@height": "11.05",
                  "#text": "Gas 6-Burner"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "586.95",
                  "@width": "22.54",
                  "@height": "9.25",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "29.03",
                  "@y": "600.74",
                  "@width": "12.29",
                  "@height": "11.05",
                  "#text": "17"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "61.69",
                  "@y": "600.74",
                  "@width": "53.55",
                  "@height": "11.05",
                  "#text": "HGR-996Z"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "148.08",
                  "@y": "600.74",
                  "@width": "58.72",
                  "@height": "11.05",
                  "#text": "Range With"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "598.22",
                  "@width": "114.62",
                  "@height": "9.25",
                  "#text": "Dimension:550*680*270mm"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "478.11",
                  "@y": "599.35",
                  "@width": "7.17",
                  "@height": "12.90",
                  "#text": "5"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "525.17",
                  "@y": "599.35",
                  "@width": "39.05",
                  "@height": "12.90",
                  "#text": "$767.6"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "609.72",
                  "@width": "114.32",
                  "@height": "9.25",
                  "#text": "LPG2800-3700Pa:2.96Kg/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "154.11",
                  "@y": "614.68",
                  "@width": "46.71",
                  "@height": "11.05",
                  "#text": "GasOven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "621.26",
                  "@width": "111.57",
                  "@height": "9.25",
                  "#text": "NG2000-2500Pa:3.98m3/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "632.77",
                  "@width": "25.76",
                  "@height": "9.25",
                  "#text": "Power"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "639.48",
                  "@width": "119.68",
                  "@height": "9.25",
                  "#text": "Dimension:1200*900*920mm"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "144.26",
                  "@y": "650.88",
                  "@width": "66.34",
                  "@height": "11.05",
                  "#text": "Gas 6-Burner"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "651.03",
                  "@width": "22.54",
                  "@height": "9.25",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "29.03",
                  "@y": "664.82",
                  "@width": "12.29",
                  "@height": "11.05",
                  "#text": "18"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "58.10",
                  "@y": "664.82",
                  "@width": "61.01",
                  "@height": "11.05",
                  "#text": "HGR-996ZA"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "128.16",
                  "@y": "664.82",
                  "@width": "98.59",
                  "@height": "11.05",
                  "#text": "Range With Electric"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "662.30",
                  "@width": "114.62",
                  "@height": "9.25",
                  "#text": "Dimension:550*680*270mm"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "478.11",
                  "@y": "663.43",
                  "@width": "7.17",
                  "@height": "12.90",
                  "#text": "5"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "525.17",
                  "@y": "663.43",
                  "@width": "39.05",
                  "@height": "12.90",
                  "#text": "$704.2"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "673.80",
                  "@width": "114.32",
                  "@height": "9.25",
                  "#text": "LPG2800-3700Pa:2.96Kg/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "164.18",
                  "@y": "678.76",
                  "@width": "26.41",
                  "@height": "11.05",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "685.35",
                  "@width": "111.57",
                  "@height": "9.25",
                  "#text": "NG2000-2500Pa:3.98m3/H"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "696.85",
                  "@width": "25.76",
                  "@height": "9.25",
                  "#text": "Power"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "706.92",
                  "@width": "119.68",
                  "@height": "9.25",
                  "#text": "Dimension:1200*900*920mm"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "143.07",
                  "@y": "714.96",
                  "@width": "68.68",
                  "@height": "11.05",
                  "#text": "Gas Range 4-"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "718.47",
                  "@width": "22.54",
                  "@height": "9.25",
                  "#text": "Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "29.03",
                  "@y": "728.90",
                  "@width": "12.29",
                  "@height": "11.05",
                  "#text": "19"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "65.05",
                  "@y": "728.90",
                  "@width": "46.80",
                  "@height": "11.05",
                  "#text": "HGR-998"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "139.94",
                  "@y": "728.90",
                  "@width": "75.04",
                  "@height": "11.05",
                  "#text": "Burner Stove &"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "729.97",
                  "@width": "114.62",
                  "@height": "9.25",
                  "#text": "Dimension:550*680*270mm"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "478.11",
                  "@y": "727.51",
                  "@width": "7.17",
                  "@height": "12.90",
                  "#text": "5"
                }
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "13.0",
                  "@x": "525.17",
                  "@y": "727.51",
                  "@width": "39.05",
                  "@height": "12.90",
                  "#text": "$753.5"
                }
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "11.0",
                  "@x": "139.43",
                  "@y": "742.84",
                  "@width": "76.10",
                  "@height": "11.05",
                  "#text": "Griddle & Oven"
                }
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "741.52",
                  "@width": "25.76",
                  "@height": "9.25",
                  "#text": "Power"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          },
          {
            "column": [
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": ""
              },
              {
                "text": {
                  "@fontName": "Arial",
                  "@fontSize": "9.0",
                  "@x": "314.66",
                  "@y": "752.79",
                  "@width": "105.10",
                  "@height": "9.25",
                  "#text": "Supply:7.5x4+5.8+5.8KW"
                }
              },
              {
                "text": ""
              },
              {
                "text": ""
              }
            ]
          }
        ]
      }
    ]
  }
}

# Convert JSON data to a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel("output.xlsx", index=False)
