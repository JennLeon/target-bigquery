schema_simple_1 = '{ "type": "SCHEMA", "stream": "simple_stream", "schema": { "properties": { "id": { "type": [ "null", "string" ] }, "name": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "integer" ] }, "ratio": { "type": [ "null", "number" ] }, "timestamp": { "type": "string", "format": "date-time" }, "date": { "type": "string", "format": "date" } }, "type": [ "null", "object" ] }, "key_properties": [ "id" ], "bookmark_properties": [ "date" ] }'


# schema_nested_1 - method 2 of schema conversion ("simplify and convert") failed

    # Simplifying function

        # input:
        # { "age": { "type": [ "null", "integer", "string" ] }

        # output of simplifying:
        # 'age': {'anyOf': [{'type': ['integer', 'null']}, {'type': ['string', 'null']}]}

        #anyOf appears this causes our conversion to fail
        # issue solved. Prioritization of data types is implemented.


schema_nested_1 =  '{ "type": "SCHEMA", "stream": "nested_stream", "schema": { "properties": { "account_id": { "type": [ "null", "string" ] }, "account_name": { "type": [ "null", "string" ] }, "action_values": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "ad_id": { "type": [ "null", "string" ] }, "ad_name": { "type": [ "null", "string" ] }, "adset_id": { "type": [ "null", "string" ] }, "adset_name": { "type": [ "null", "string" ] }, "age": { "type": [ "null", "integer", "string" ] }, "campaign_id": { "type": [ "null", "string" ] }, "campaign_name": { "type": [ "null", "string" ] }, "canvas_avg_view_percent": { "type": [ "null", "number" ] }, "canvas_avg_view_time": { "type": [ "null", "number" ] }, "clicks": { "type": [ "null", "integer" ] }, "conversion_rate_ranking": { "type": [ "null", "string" ] }, "cost_per_action_type": { "items": { "properties": { "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "string" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "cost_per_inline_link_click": { "type": [ "null", "number" ] }, "cost_per_inline_post_engagement": { "type": [ "null", "number" ] }, "cost_per_unique_action_type": { "items": { "properties": { "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "string" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "cost_per_unique_click": { "type": [ "null", "number" ] }, "cost_per_unique_inline_link_click": { "type": [ "null", "number" ] }, "cpc": { "type": [ "null", "number" ] }, "cpm": { "type": [ "null", "number" ] }, "cpp": { "type": [ "null", "number" ] }, "ctr": { "type": [ "null", "number" ] }, "date_start": { "format": "date-time", "type": [ "null", "string" ] }, "date_stop": { "format": "date-time", "type": [ "null", "string" ] }, "engagement_rate_ranking": { "type": [ "null", "string" ] }, "frequency": { "type": [ "null", "number" ] }, "gender": { "type": [ "null", "string" ] }, "impressions": { "type": [ "null", "integer" ] }, "inline_link_click_ctr": { "type": [ "null", "number" ] }, "inline_link_clicks": { "type": [ "null", "integer" ] }, "inline_post_engagement": { "type": [ "null", "integer" ] }, "objective": { "type": [ "null", "string" ] }, "outbound_clicks": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "quality_ranking": { "type": [ "null", "string" ] }, "reach": { "type": [ "null", "integer" ] }, "social_spend": { "type": [ "null", "number" ] }, "spend": { "type": [ "null", "number" ] }, "unique_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "unique_clicks": { "type": [ "null", "integer" ] }, "unique_ctr": { "type": [ "null", "number" ] }, "unique_inline_link_click_ctr": { "type": [ "null", "number" ] }, "unique_inline_link_clicks": { "type": [ "null", "integer" ] }, "unique_link_clicks_ctr": { "type": [ "null", "number" ] }, "video_30_sec_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_p100_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_p25_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_p50_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_p75_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_play_curve_actions": { "items": { "properties": { "action_type": { "type": [ "null", "string" ] }, "value": { "items": { "type": [ "null", "integer" ] }, "type": [ "null", "array" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "website_ctr": { "items": { "properties": { "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] } }, "type": [ "null", "object" ] }, "key_properties": [ "campaign_id", "adset_id", "ad_id", "date_start", "age", "gender" ], "bookmark_properties": [ "date_start" ] }'



# made-up schema - collection of columns with anyOf
test_schema_collection_anyOf_problem_column =  """{ "type": "SCHEMA", "stream": "nested_stream", "schema": { "properties": 

{ 
  
    "test_column_no_anyOf": { "items": { "properties": { "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] },


    "BiddingScheme": {"anyOf": [{"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "InheritedBidStrategyType": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}, "TargetCpa": {"type": ["null", "number"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "TargetRoas": {"type": ["null", "number"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}, "TargetRoas": {"type": ["null", "number"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}, "TargetAdPosition": {"type": ["null", "string"]}, "TargetImpressionShare": {"type": ["null", "number"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}}}]}, 

    "Settings": {"type": ["null", "object"], "properties": {"Setting": {"type": ["null", "array"], "items": {"anyOf": [{"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "Details": {"type": ["null", "object"], "properties": {"TargetSettingDetail": {"type": ["null", "array"], "items": {"type": ["null", "object"], "additionalProperties": false, "properties": {"CriterionTypeGroup": {"type": ["null", "string"]}, "TargetAndBid": {"type": ["boolean"]}}}}}}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "LocalInventoryAdsEnabled": {"type": ["null", "boolean"]}, "Priority": {"type": ["null", "integer"]}, "SalesCountryCode": {"type": ["null", "string"]}, "StoreId": {"type": ["null", "integer"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "BidBoostValue": {"type": ["null", "number"]}, "BidMaxValue": {"type": ["null", "number"]}, "BidOption": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "DomainName": {"type": ["null", "string"]}, "Language": {"type": ["null", "string"]}, "PageFeedIds": {"type": ["null", "object"], "properties": {"long": {"type": ["null", "array"], "items": {"type": "integer"}}}}, "Source": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}}}]}}}}, 


    "discount_codes": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "amount": {                      "type": [                        "null",                        "number"                      ]                    },                    "code": {                      "type": [                        "null",                        "string"                      ]                    },                    "type": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          }, 



    "line_items": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "grams": {                      "type": [                        "null",                        "integer"                      ]                    },                    "images": {                      "type": [                        "null",                        "object"                      ],                      "additionalProperties": false,                      "properties": {                        "large": {                          "type": [                            "null",                            "string"                          ]                        },                        "medium": {                          "type": [                            "null",                            "string"                          ]                        },                        "original": {                          "type": [                            "null",                            "string"                          ]                        },                        "small": {                          "type": [                            "null",                            "string"                          ]                        }                      }                    },                    "price": {                      "type": [                        "null",                        "number"                      ],                      "multipleOf": 1e-08                    },                    "properties": {                      "anyOf": [                        {                          "type": "array",                          "items": {                            "type": "object",                            "additionalProperties": false,                            "properties": {                              "name": {                                "type": [                                  "null",                                  "string"                                ]                              },                              "value": {                                "type": [                                  "null",                                  "string"                                ]                              }                            }                          }                        },                        {                          "type": "null"                        }                      ]                    },                    "quantity": {                      "type": [                        "null",                        "integer"                      ]                    },                    "shopify_product_id": {                      "type": [                        "null",                        "string"                      ]                    },                    "shopify_variant_id": {                      "type": [                        "null",                        "string"                      ]                    },                    "sku": {                      "type": [                        "null",                        "string"                      ]                    },                    "subscription_id": {                      "type": [                        "null",                        "string"                      ]                    },                    "title": {                      "type": [                        "null",                        "string"                      ]                    },                    "variant_title": {                      "type": [                        "null",                        "string"                      ]                    },                    "vendor": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          }, 



    "shipping_lines": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "code": {                      "type": [                        "null",                        "string"                      ]                    },                    "price": {                      "type": [                        "null",                        "number"                      ]                    },                    "title": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          }, 


    "tax_lines": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "code": {                      "type": [                        "null",                        "string"                      ]                    },                    "price": {                      "type": [                        "null",                        "number"                      ]                    },                    "title": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          },


    "note_attributes": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "name": {                      "type": [                        "null",                        "string"                      ]                    },                    "value": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          },

    "simplification_stage_adds_anyOf": { "type": [ "null", "integer", "string" ] }

   

    
}, "type": [ "null", "object" ] }, "key_properties": [ "campaign_id", "adset_id", "ad_id", "date_start", "age", "gender" ], "bookmark_properties": [ "date_start" ] }"""



# if a column has "items", but doesn't have "properties" inside, it  created an issue while re-writing schema.py to make it simpler. Issue has been handled.
schema_nested_1_subset_items_problem =  '{ "type": "SCHEMA", "stream": "nested_stream", "schema": { "properties": {"video_play_curve_actions": { "items": { "properties": { "action_type": { "type": [ "null", "string" ] }, "problem_field": { "items": { "type": [ "null", "integer" ] }, "type": [ "null", "array" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "website_ctr": { "items": { "properties": { "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] } }, "type": [ "null", "object" ] }, "key_properties": [ "campaign_id", "adset_id", "ad_id", "date_start", "age", "gender" ], "bookmark_properties": [ "date_start" ] }'


schema_nested_2 = '{"type": "SCHEMA", "stream": "campaigns", "schema": {"type": ["null", "object"], "additionalProperties": false, "properties": {"AudienceAdsBidAdjustment": {"type": ["null", "integer"]}, "BiddingScheme": {"anyOf": [{"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "InheritedBidStrategyType": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}, "TargetCpa": {"type": ["null", "number"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "TargetRoas": {"type": ["null", "number"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}, "TargetRoas": {"type": ["null", "number"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}, "TargetAdPosition": {"type": ["null", "string"]}, "TargetImpressionShare": {"type": ["null", "number"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}}}]}, "BudgetType": {"type": ["null", "string"]}, "DailyBudget": {"type": ["null", "number"]}, "ExperimentId": {"type": ["null", "integer"]}, "FinalUrlSuffix": {"type": ["null", "string"]}, "ForwardCompatibilityMap": {"type": ["null", "object"], "properties": {"KeyValuePairOfstringstring": {"type": ["null", "array"], "items": {"type": ["null", "object"], "additionalProperties": false, "properties": {"key": {"type": ["null", "string"]}, "value": {"type": ["null", "string"]}}}}}}, "Id": {"type": ["null", "integer"]}, "Name": {"type": ["null", "string"]}, "Status": {"type": ["null", "string"]}, "SubType": {"type": ["null", "string"]}, "TimeZone": {"type": ["null", "string"]}, "TrackingUrlTemplate": {"type": ["null", "string"]}, "UrlCustomParameters": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Parameters": {"type": ["null", "object"], "properties": {"CustomParameter": {"type": ["null", "array"], "items": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Key": {"type": ["null", "string"]}, "Value": {"type": ["null", "string"]}}}}}}}}, "CampaignType": {"type": ["null", "string"]}, "Settings": {"type": ["null", "object"], "properties": {"Setting": {"type": ["null", "array"], "items": {"anyOf": [{"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "Details": {"type": ["null", "object"], "properties": {"TargetSettingDetail": {"type": ["null", "array"], "items": {"type": ["null", "object"], "additionalProperties": false, "properties": {"CriterionTypeGroup": {"type": ["null", "string"]}, "TargetAndBid": {"type": ["boolean"]}}}}}}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "LocalInventoryAdsEnabled": {"type": ["null", "boolean"]}, "Priority": {"type": ["null", "integer"]}, "SalesCountryCode": {"type": ["null", "string"]}, "StoreId": {"type": ["null", "integer"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "BidBoostValue": {"type": ["null", "number"]}, "BidMaxValue": {"type": ["null", "number"]}, "BidOption": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "DomainName": {"type": ["null", "string"]}, "Language": {"type": ["null", "string"]}, "PageFeedIds": {"type": ["null", "object"], "properties": {"long": {"type": ["null", "array"], "items": {"type": "integer"}}}}, "Source": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}}}]}}}}, "BudgetId": {"type": ["null", "integer"]}, "Languages": {"type": ["null", "object"], "properties": {"string": {"type": ["null", "array"], "items": {"type": "string"}}}}, "AdScheduleUseSearcherTimeZone": {"type": ["null", "boolean"]}}}, "key_properties": ["Id"]}'


schema_nested_3_shopify = '{    "type":"SCHEMA",    "stream":"orders",    "schema": {        "properties": {          "address_id": {            "type": [              "null",              "string"            ]          },          "address_is_active": {            "type": [              "null",              "boolean"            ]          },          "billing_address": {            "properties": {              "address1": {                "type": [                  "null",                  "string"                ]              },              "address2": {                "type": [                  "null",                  "string"                ]              },              "city": {                "type": [                  "null",                  "string"                ]              },              "company": {                "type": [                  "null",                  "string"                ]              },              "country": {                "type": [                  "null",                  "string"                ]              },              "first_name": {                "type": [                  "null",                  "string"                ]              },              "last_name": {                "type": [                  "null",                  "string"                ]              },              "phone": {                "type": [                  "null",                  "string"                ]              },              "province": {                "type": [                  "null",                  "string"                ]              },              "zip": {                "type": [                  "null",                  "string"                ]              }            },            "type": [              "null",              "object"            ],            "additionalProperties": false          },          "charge_id": {            "type": [              "null",              "string"            ]          },          "charge_status": {            "type": [              "null",              "string"            ]          },          "created_at": {            "format": "date-time",            "type": [              "null",              "string"            ]          },          "customer_id": {            "type": [              "null",              "string"            ]          },          "discount_codes": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "amount": {                      "type": [                        "null",                        "number"                      ]                    },                    "code": {                      "type": [                        "null",                        "string"                      ]                    },                    "type": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          },          "email": {            "type": [              "null",              "string"            ]          },          "first_name": {            "type": [              "null",              "string"            ]          },          "hash": {            "type": [              "null",              "string"            ]          },          "id": {            "type": [              "null",              "string"            ]          },          "is_prepaid": {            "type": [              "null",              "boolean"            ]          },          "last_name": {            "type": [              "null",              "string"            ]          },          "line_items": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "grams": {                      "type": [                        "null",                        "integer"                      ]                    },                    "images": {                      "type": [                        "null",                        "object"                      ],                      "additionalProperties": false,                      "properties": {                        "large": {                          "type": [                            "null",                            "string"                          ]                        },                        "medium": {                          "type": [                            "null",                            "string"                          ]                        },                        "original": {                          "type": [                            "null",                            "string"                          ]                        },                        "small": {                          "type": [                            "null",                            "string"                          ]                        }                      }                    },                    "price": {                      "type": [                        "null",                        "number"                      ],                      "multipleOf": 1e-08                    },                    "properties": {                      "anyOf": [                        {                          "type": "array",                          "items": {                            "type": "object",                            "additionalProperties": false,                            "properties": {                              "name": {                                "type": [                                  "null",                                  "string"                                ]                              },                              "value": {                                "type": [                                  "null",                                  "string"                                ]                              }                            }                          }                        },                        {                          "type": "null"                        }                      ]                    },                    "quantity": {                      "type": [                        "null",                        "integer"                      ]                    },                    "shopify_product_id": {                      "type": [                        "null",                        "string"                      ]                    },                    "shopify_variant_id": {                      "type": [                        "null",                        "string"                      ]                    },                    "sku": {                      "type": [                        "null",                        "string"                      ]                    },                    "subscription_id": {                      "type": [                        "null",                        "string"                      ]                    },                    "title": {                      "type": [                        "null",                        "string"                      ]                    },                    "variant_title": {                      "type": [                        "null",                        "string"                      ]                    },                    "vendor": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          },          "note": {            "type": [              "null",              "string"            ]          },          "note_attributes": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "name": {                      "type": [                        "null",                        "string"                      ]                    },                    "value": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          },          "payment_processor": {            "type": [              "null",              "string"            ]          },          "processed_at": {            "format": "date-time",            "type": [              "null",              "string"            ]          },          "scheduled_at": {            "format": "date-time",            "type": [              "null",              "string"            ]          },          "shipped_date": {            "format": "date-time",            "type": [              "null",              "string"            ]          },          "shipping_address": {            "properties": {              "address1": {                "type": [                  "null",                  "string"                ]              },              "address2": {                "type": [                  "null",                  "string"                ]              },              "city": {                "type": [                  "null",                  "string"                ]              },              "company": {                "type": [                  "null",                  "string"                ]              },              "country": {                "type": [                  "null",                  "string"                ]              },              "first_name": {                "type": [                  "null",                  "string"                ]              },              "last_name": {                "type": [                  "null",                  "string"                ]              },              "phone": {                "type": [                  "null",                  "string"                ]              },              "province": {                "type": [                  "null",                  "string"                ]              },              "zip": {                "type": [                  "null",                  "string"                ]              }            },            "type": [              "null",              "object"            ],            "additionalProperties": false          },          "shipping_date": {            "format": "date-time",            "type": [              "null",              "string"            ]          },          "shipping_lines": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "code": {                      "type": [                        "null",                        "string"                      ]                    },                    "price": {                      "type": [                        "null",                        "number"                      ]                    },                    "title": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          },          "shopify_cart_token": {            "type": [              "null",              "string"            ]          },          "shopify_customer_id": {            "type": [              "null",              "string"            ]          },          "shopify_id": {            "type": [              "null",              "string"            ]          },          "shopify_order_id": {            "type": [              "null",              "string"            ]          },          "shopify_order_number": {            "type": [              "null",              "string"            ]          },          "status": {            "type": [              "null",              "string"            ]          },          "subtotal_price": {            "type": [              "null",              "number"            ]          },          "tags": {            "type": [              "null",              "string"            ]          },          "tax_lines": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "code": {                      "type": [                        "null",                        "string"                      ]                    },                    "price": {                      "type": [                        "null",                        "number"                      ]                    },                    "title": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          },          "total_discounts": {            "multipleOf": 1e-08,            "type": [              "null",              "number"            ]          },          "total_line_items_price": {            "multipleOf": 1e-08,            "type": [              "null",              "number"            ]          },          "total_price": {            "type": [              "null",              "number"            ]          },          "total_refunds": {            "multipleOf": 1e-08,            "type": [              "null",              "number"            ]          },          "total_tax": {            "multipleOf": 1e-08,            "type": [              "null",              "number"            ]          },          "total_weight": {            "type": [              "null",              "integer"            ]          },          "transaction_id": {            "type": [              "null",              "string"            ]          },          "type": {            "type": [              "null",              "string"            ]          },          "updated_at": {            "format": "date-time",            "type": [              "null",              "string"            ]          }        },        "type": "object",        "additionalProperties": false      },    "key_properties":[       "Id"    ] }'




# Bing Ads accounts

"""
This is invalid schema

This table has KeyValueOfstringbase column.
It previously created an issue, while using method 1 of schema conversion.

I figured out how to solve the problem in Bing Ads column KeyValueOfstringbase, aka KeyValuePairOfstringbase, aka KeyValuePairOfstringbase64Binary (it got renamed).

Schema conversion (JSON → BigQuery) was failing, because tap-bing-ads was generating incorrect schema for this column.

Solution:

Replace:
pip install tap-bing-ads==2.0.15
with
pip install tap-bing-ads==2.0.16

I tested, all data gets loaded successfully, including the problem column

"""

bing_ads_accounts = '{"type":"SCHEMA","stream":"accounts","schema":{"type":["null","object"],"additionalProperties":false,"properties":{"BillToCustomerId":{"type":["null","integer"]},"CurrencyCode":{"type":["null","string"]},"AccountFinancialStatus":{"type":["null","string"]},"Id":{"type":["null","integer"]},"Language":{"type":["null","string"]},"LastModifiedByUserId":{"type":["null","integer"]},"LastModifiedTime":{"type":["null","string"],"format":"date-time"},"Name":{"type":["null","string"]},"Number":{"type":["null","string"]},"ParentCustomerId":{"type":["integer"]},"PaymentMethodId":{"type":["null","integer"]},"PaymentMethodType":{"type":["null","string"]},"PrimaryUserId":{"type":["null","integer"]},"AccountLifeCycleStatus":{"type":["null","string"]},"TimeStamp":{"type":["null","string"]},"TimeZone":{"type":["null","string"]},"PauseReason":{"type":["null","integer"]},"ForwardCompatibilityMap":{"type":["null","object"],"properties":{"KeyValuePairOfstringstring":{"type":["null","array"],"items":{"type":["null","object"],"additionalProperties":false,"properties":{"key":{"type":["null","string"]},"value":{"type":["null","string"]}}}}}},"LinkedAgencies":{"type":["null","object"],"properties":{"CustomerInfo":{"type":["null","array"],"items":{"type":["null","object"],"additionalProperties":false,"properties":{"Id":{"type":["null","integer"]},"Name":{"type":["null","string"]}}}}}},"SalesHouseCustomerId":{"type":["null","integer"]},"TaxInformation":{"type":["null","object"],"properties":{"KeyValuePairOfstringstring":{"type":["null","array"],"items":{"type":["null","object"],"additionalProperties":false,"properties":{"key":{"type":["null","string"]},"value":{"type":["null","string"]}}}}}},"BackUpPaymentInstrumentId":{"type":["null","integer"]},"BillingThresholdAmount":{"type":["null","number"]},"BusinessAddress":{"type":["null","object"],"additionalProperties":false,"properties":{"City":{"type":["null","string"]},"CountryCode":{"type":["null","string"]},"Id":{"type":["null","integer"]},"Line1":{"type":["null","string"]},"Line2":{"type":["null","string"]},"Line3":{"type":["null","string"]},"Line4":{"type":["null","string"]},"PostalCode":{"type":["null","string"]},"StateOrProvince":{"type":["null","string"]},"TimeStamp":{"type":["null","string"]},"BusinessName":{"type":["null","string"]}}},"AutoTagType":{"type":["null","string"]},"SoldToPaymentInstrumentId":{"type":["null","integer"]},"TaxCertificate":{"type":["null","object"],"additionalProperties":false,"properties":{"TaxCertificateBlobContainerName":{"type":["null","string"]},"TaxCertificates":{"type":["null","object"],"properties":{"KeyValueOfstringbase":{"type":["null","array"],"items":"KeyValueOfstringbase"}}},"Status":{"type":["null","string"]}}}}},"key_properties":[]}'



bing_ads_accounts_shorter_version = """
{"type":"SCHEMA",

"stream":"accounts",

"schema":

    {"type":["null","object"],

        "additionalProperties":false,

        "properties":{
            
            "SoldToPaymentInstrumentId":{"type":["null","integer"]},
            
            "TaxCertificate":{"type":["null","object"],"additionalProperties":false,"properties":{
                "TaxCertificateBlobContainerName":{"type":["null","string"]}, 

                "TaxCertificates":{"type":["null","object"],"properties": {
                    "KeyValueOfstringbase":{"type":["null","array"],"items":"KeyValueOfstringbase"}}},

                "Status":{"type":["null","string"]}}
                            }
        
        }
    
    },"key_properties":[]
    
}
"""


# this is the version from Adserve Bing Ads tap implementation:
bing_ads_accounts_v2 = """{
      "tap_stream_id": "accounts",
      "stream": "accounts",
      "schema": { "selected":true,
        "type": [
          "null",
          "object"
        ],
        "additionalProperties": false,
        "properties": {
          "BillToCustomerId": {
            "type": [
              "null",
              "integer"
            ]
          },
          "CurrencyCode": {
            "type": [
              "null",
              "string"
            ]
          },
          "AccountFinancialStatus": {
            "type": [
              "null",
              "string"
            ]
          },
          "Id": {
            "type": [
              "null",
              "integer"
            ]
          },
          "Language": {
            "type": [
              "null",
              "string"
            ]
          },
          "LastModifiedByUserId": {
            "type": [
              "null",
              "integer"
            ]
          },
          "LastModifiedTime": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "Name": {
            "type": [
              "null",
              "string"
            ]
          },
          "Number": {
            "type": [
              "null",
              "string"
            ]
          },
          "ParentCustomerId": {
            "type": [
              "integer"
            ]
          },
          "PaymentMethodId": {
            "type": [
              "null",
              "integer"
            ]
          },
          "PaymentMethodType": {
            "type": [
              "null",
              "string"
            ]
          },
          "PrimaryUserId": {
            "type": [
              "null",
              "integer"
            ]
          },
          "AccountLifeCycleStatus": {
            "type": [
              "null",
              "string"
            ]
          },
          "TimeStamp": {
            "type": [
              "null",
              "string"
            ]
          },
          "TimeZone": {
            "type": [
              "null",
              "string"
            ]
          },
          "PauseReason": {
            "type": [
              "null",
              "integer"
            ]
          },
          "ForwardCompatibilityMap": {
            "type": [
              "null",
              "object"
            ],
            "properties": {
              "KeyValuePairOfstringstring": {
                "type": [
                  "null",
                  "array"
                ],
                "items": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "key": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "value": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                }
              }
            }
          },
          "LinkedAgencies": {
            "type": [
              "null",
              "object"
            ],
            "properties": {
              "CustomerInfo": {
                "type": [
                  "null",
                  "array"
                ],
                "items": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Id": {
                      "type": [
                        "null",
                        "integer"
                      ]
                    },
                    "Name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                }
              }
            }
          },
          "SalesHouseCustomerId": {
            "type": [
              "null",
              "integer"
            ]
          },
          "TaxInformation": {
            "type": [
              "null",
              "object"
            ],
            "properties": {
              "KeyValuePairOfstringstring": {
                "type": [
                  "null",
                  "array"
                ],
                "items": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "key": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "value": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                }
              }
            }
          },
          "BackUpPaymentInstrumentId": {
            "type": [
              "null",
              "integer"
            ]
          },
          "BillingThresholdAmount": {
            "type": [
              "null",
              "number"
            ]
          },
          "BusinessAddress": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "City": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "CountryCode": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "Id": {
                "type": [
                  "null",
                  "integer"
                ]
              },
              "Line1": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "Line2": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "Line3": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "Line4": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "PostalCode": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "StateOrProvince": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "TimeStamp": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "BusinessName": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "AutoTagType": {
            "type": [
              "null",
              "string"
            ]
          },
          "SoldToPaymentInstrumentId": {
            "type": [
              "null",
              "integer"
            ]
          }
        }
      },
      "key_properties": [
        "Id",
        "LastModifiedTime"
      ],
      "replication_key": "LastModifiedTime",
      "replication_method": "INCREMENTAL",
      "metadata": [
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "PaymentMethodId"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "PrimaryUserId"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "CurrencyCode"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "Number"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "LinkedAgencies"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "ForwardCompatibilityMap"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "AutoTagType"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "LastModifiedByUserId"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "SoldToPaymentInstrumentId"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "Name"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "PaymentMethodType"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "TimeStamp"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "ParentCustomerId"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "TaxInformation"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "BillingThresholdAmount"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "BusinessAddress"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "TimeZone"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "BackUpPaymentInstrumentId"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "PauseReason"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "BillToCustomerId"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "AccountLifeCycleStatus"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "SalesHouseCustomerId"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "AccountFinancialStatus"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "Language"
          ]
        }
      ]
    }"""

# Bing Ads campaigns

bing_ads_campaigns = '{"type":"SCHEMA","stream":"campaigns","schema":{"type":["null","object"],"additionalProperties":false,"properties":{"AudienceAdsBidAdjustment":{"type":["null","integer"]},"BiddingScheme":{"anyOf":[{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"MaxCpc":{"type":["null","object"],"additionalProperties":false,"properties":{"Amount":{"type":["null","number"]}}},"TargetRoas":{"type":["null","number"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"MaxCpc":{"type":["null","object"],"additionalProperties":false,"properties":{"Amount":{"type":["null","number"]}}}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"MaxCpc":{"type":["null","object"],"additionalProperties":false,"properties":{"Amount":{"type":["null","number"]}}}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"InheritedBidStrategyType":{"type":["null","string"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"MaxCpc":{"type":["null","object"],"additionalProperties":false,"properties":{"Amount":{"type":["null","number"]}}}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"MaxCpc":{"type":["null","object"],"additionalProperties":false,"properties":{"Amount":{"type":["null","number"]}}},"TargetAdPosition":{"type":["null","string"]},"TargetImpressionShare":{"type":["null","number"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"TargetRoas":{"type":["null","number"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"MaxCpc":{"type":["null","object"],"additionalProperties":false,"properties":{"Amount":{"type":["null","number"]}}},"TargetCpa":{"type":["null","number"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]}}}]},"BudgetType":{"type":["null","string"]},"DailyBudget":{"type":["null","number"]},"ExperimentId":{"type":["null","integer"]},"FinalUrlSuffix":{"type":["null","string"]},"ForwardCompatibilityMap":{"type":["null","object"],"properties":{"KeyValuePairOfstringstring":{"type":["null","array"],"items":{"type":["null","object"],"additionalProperties":false,"properties":{"key":{"type":["null","string"]},"value":{"type":["null","string"]}}}}}},"Id":{"type":["null","integer"]},"Name":{"type":["null","string"]},"Status":{"type":["null","string"]},"SubType":{"type":["null","string"]},"TimeZone":{"type":["null","string"]},"TrackingUrlTemplate":{"type":["null","string"]},"UrlCustomParameters":{"type":["null","object"],"additionalProperties":false,"properties":{"Parameters":{"type":["null","object"],"properties":{"CustomParameter":{"type":["null","array"],"items":{"type":["null","object"],"additionalProperties":false,"properties":{"Key":{"type":["null","string"]},"Value":{"type":["null","string"]}}}}}}}},"CampaignType":{"type":["null","string"]},"Settings":{"type":["null","object"],"properties":{"Setting":{"type":["null","array"],"items":{"anyOf":[{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"DomainName":{"type":["null","string"]},"Language":{"type":["null","string"]},"PageFeedIds":{"type":["null","object"],"properties":{"long":{"type":["null","array"],"items":{"type":"integer"}}}},"Source":{"type":["null","string"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"Details":{"type":["null","object"],"properties":{"TargetSettingDetail":{"type":["null","array"],"items":{"type":["null","object"],"additionalProperties":false,"properties":{"CriterionTypeGroup":{"type":["null","string"]},"TargetAndBid":{"type":["boolean"]}}}}}}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"LocalInventoryAdsEnabled":{"type":["null","boolean"]},"Priority":{"type":["null","integer"]},"SalesCountryCode":{"type":["null","string"]},"StoreId":{"type":["null","integer"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"BidBoostValue":{"type":["null","number"]},"BidMaxValue":{"type":["null","number"]},"BidOption":{"type":["null","string"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]}}}]}}}},"BudgetId":{"type":["null","integer"]},"Languages":{"type":["null","object"],"properties":{"string":{"type":["null","array"],"items":{"type":"string"}}}},"AdScheduleUseSearcherTimeZone":{"type":["null","boolean"]}}},"key_properties":[]}'


# Bing Ads ad_extension_detail_report

bing_ads_ad_extension_detail_report = '{"type":"SCHEMA","stream":"ad_extension_detail_report","schema":{"properties":{"AccountName":{"type":["null","string"]},"AccountId":{"type":["null","integer"]},"TimePeriod":{"type":["null","string"],"format":"date-time"},"CampaignName":{"type":["null","string"]},"CampaignId":{"type":["null","integer"]},"AdGroupName":{"type":["null","string"]},"AdGroupId":{"type":["null","integer"]},"AdTitle":{"type":["null","string"]},"AdId":{"type":["null","integer"]},"AdExtensionType":{"type":["null","string"]},"AdExtensionTypeId":{"type":["null","string"]},"AdExtensionId":{"type":["null","string"]},"AdExtensionVersion":{"type":["null","string"]},"AdExtensionPropertyValue":{"type":["null","string"]},"Impressions":{"type":["null","integer"]},"DeviceType":{"type":["null","string"]},"DeviceOS":{"type":["null","string"]},"Clicks":{"type":["null","integer"]},"Ctr":{"type":["null","number"]},"Conversions":{"type":["null","number"]},"CostPerConversion":{"type":["null","number"]},"ConversionRate":{"type":["null","number"]},"Spend":{"type":["null","number"]},"AverageCpc":{"type":["null","number"]},"BidMatchType":{"type":["null","string"]},"DeliveredMatchType":{"type":["null","string"]},"Network":{"type":["null","string"]},"TopVsOther":{"type":["null","string"]},"Assists":{"type":["null","integer"]},"Revenue":{"type":["null","number"]},"ReturnOnAdSpend":{"type":["null","number"]},"CostPerAssist":{"type":["null","number"]},"RevenuePerConversion":{"type":["null","number"]},"RevenuePerAssist":{"type":["null","number"]},"AccountStatus":{"type":["null","string"]},"CampaignStatus":{"type":["null","string"]},"AdGroupStatus":{"type":["null","string"]},"AdStatus":{"type":["null","string"]},"AllConversions":{"type":["null","string"]},"AllRevenue":{"type":["null","string"]},"AllConversionRate":{"type":["null","string"]},"AllCostPerConversion":{"type":["null","string"]},"AllReturnOnAdSpend":{"type":["null","string"]},"AllRevenuePerConversion":{"type":["null","string"]},"Goal":{"type":["null","string"]},"GoalType":{"type":["null","string"]},"_sdc_report_datetime":{"type":"string","format":"date-time"}},"additionalProperties":false,"type":"object"},"key_properties":[]}'


# Bing Ads ad_group_performance_report

bing_ads_ad_group_performance_report = '{"type":"SCHEMA","stream":"ad_group_performance_report","schema":{"properties":{"AccountName":{"type":["null","string"]},"AccountNumber":{"type":["null","string"]},"AccountId":{"type":["null","integer"]},"TimePeriod":{"type":["null","string"],"format":"date-time"},"Status":{"type":["null","string"]},"CampaignName":{"type":["null","string"]},"CampaignId":{"type":["null","integer"]},"AdGroupName":{"type":["null","string"]},"AdGroupId":{"type":["null","integer"]},"CurrencyCode":{"type":["null","string"]},"AdDistribution":{"type":["null","string"]},"Impressions":{"type":["null","integer"]},"Clicks":{"type":["null","integer"]},"Ctr":{"type":["null","number"]},"AverageCpc":{"type":["null","number"]},"Spend":{"type":["null","number"]},"AveragePosition":{"type":["null","number"]},"Conversions":{"type":["null","number"]},"ConversionRate":{"type":["null","number"]},"CostPerConversion":{"type":["null","number"]},"DeviceType":{"type":["null","string"]},"Language":{"type":["null","string"]},"DeviceOS":{"type":["null","string"]},"ImpressionSharePercent":{"type":["null","number"]},"ImpressionLostToBudgetPercent":{"type":["null","number"]},"ImpressionLostToRankAggPercent":{"type":["null","string"]},"QualityScore":{"type":["null","number"]},"ExpectedCtr":{"type":["null","number"]},"AdRelevance":{"type":["null","number"]},"LandingPageExperience":{"type":["null","number"]},"HistoricalQualityScore":{"type":["null","string"]},"HistoricalExpectedCtr":{"type":["null","string"]},"HistoricalAdRelevance":{"type":["null","string"]},"HistoricalLandingPageExperience":{"type":["null","string"]},"PhoneImpressions":{"type":["null","integer"]},"PhoneCalls":{"type":["null","integer"]},"Ptr":{"type":["null","number"]},"Network":{"type":["null","string"]},"TopVsOther":{"type":["null","string"]},"BidMatchType":{"type":["null","string"]},"DeliveredMatchType":{"type":["null","string"]},"Assists":{"type":["null","integer"]},"Revenue":{"type":["null","number"]},"ReturnOnAdSpend":{"type":["null","number"]},"CostPerAssist":{"type":["null","number"]},"RevenuePerConversion":{"type":["null","number"]},"RevenuePerAssist":{"type":["null","number"]},"TrackingTemplate":{"type":["null","string"]},"CustomParameters":{"type":["null","string"]},"AccountStatus":{"type":["null","string"]},"CampaignStatus":{"type":["null","string"]},"AdGroupLabels":{"type":["null","string"]},"ExactMatchImpressionSharePercent":{"type":["null","number"]},"CustomerId":{"type":["null","string"]},"CustomerName":{"type":["null","string"]},"ClickSharePercent":{"type":["null","string"]},"AbsoluteTopImpressionSharePercent":{"type":["null","string"]},"FinalUrlSuffix":{"type":["null","string"]},"CampaignType":{"type":["null","string"]},"TopImpressionShareLostToRankPercent":{"type":["null","string"]},"TopImpressionShareLostToBudgetPercent":{"type":["null","string"]},"AbsoluteTopImpressionShareLostToRankPercent":{"type":["null","string"]},"AbsoluteTopImpressionShareLostToBudgetPercent":{"type":["null","string"]},"TopImpressionSharePercent":{"type":["null","string"]},"AbsoluteTopImpressionRatePercent":{"type":["null","string"]},"TopImpressionRatePercent":{"type":["null","string"]},"BaseCampaignId":{"type":["null","string"]},"AllConversions":{"type":["null","string"]},"AllRevenue":{"type":["null","string"]},"AllConversionRate":{"type":["null","string"]},"AllCostPerConversion":{"type":["null","string"]},"AllReturnOnAdSpend":{"type":["null","string"]},"AllRevenuePerConversion":{"type":["null","string"]},"ViewThroughConversions":{"type":["null","string"]},"Goal":{"type":["null","string"]},"GoalType":{"type":["null","string"]},"AudienceImpressionSharePercent":{"type":["null","string"]},"AudienceImpressionLostToRankPercent":{"type":["null","string"]},"AudienceImpressionLostToBudgetPercent":{"type":["null","string"]},"RelativeCtr":{"type":["null","string"]},"AdGroupType":{"type":["null","string"]},"_sdc_report_datetime":{"type":"string","format":"date-time"}},"additionalProperties":false,"type":"object"},"key_properties":[]}'

# Bing Ads ad_performance_report

bing_ads_ad_performance_report = '{"type":"SCHEMA","stream":"ad_performance_report","schema":{"properties":{"AccountName":{"type":["null","string"]},"AccountNumber":{"type":["null","string"]},"AccountId":{"type":["null","integer"]},"TimePeriod":{"type":["null","string"],"format":"date-time"},"CampaignName":{"type":["null","string"]},"CampaignId":{"type":["null","integer"]},"AdGroupName":{"type":["null","string"]},"AdId":{"type":["null","integer"]},"AdGroupId":{"type":["null","integer"]},"AdTitle":{"type":["null","string"]},"AdDescription":{"type":["null","string"]},"AdDescription2":{"type":["null","string"]},"AdType":{"type":["null","string"]},"CurrencyCode":{"type":["null","string"]},"AdDistribution":{"type":["null","string"]},"Impressions":{"type":["null","integer"]},"Clicks":{"type":["null","integer"]},"Ctr":{"type":["null","number"]},"AverageCpc":{"type":["null","number"]},"Spend":{"type":["null","number"]},"AveragePosition":{"type":["null","number"]},"Conversions":{"type":["null","number"]},"ConversionRate":{"type":["null","number"]},"CostPerConversion":{"type":["null","number"]},"DestinationUrl":{"type":["null","string"]},"DeviceType":{"type":["null","string"]},"Language":{"type":["null","string"]},"DisplayUrl":{"type":["null","string"]},"AdStatus":{"type":["null","string"]},"Network":{"type":["null","string"]},"TopVsOther":{"type":["null","string"]},"BidMatchType":{"type":["null","string"]},"DeliveredMatchType":{"type":["null","string"]},"DeviceOS":{"type":["null","string"]},"Assists":{"type":["null","integer"]},"Revenue":{"type":["null","number"]},"ReturnOnAdSpend":{"type":["null","number"]},"CostPerAssist":{"type":["null","number"]},"RevenuePerConversion":{"type":["null","number"]},"RevenuePerAssist":{"type":["null","number"]},"TrackingTemplate":{"type":["null","string"]},"CustomParameters":{"type":["null","string"]},"FinalUrl":{"type":["null","string"]},"FinalMobileUrl":{"type":["null","string"]},"FinalAppUrl":{"type":["null","string"]},"AccountStatus":{"type":["null","string"]},"CampaignStatus":{"type":["null","string"]},"AdGroupStatus":{"type":["null","string"]},"TitlePart1":{"type":["null","string"]},"TitlePart2":{"type":["null","string"]},"TitlePart3":{"type":["null","string"]},"Headline":{"type":["null","string"]},"LongHeadline":{"type":["null","string"]},"BusinessName":{"type":["null","string"]},"Path1":{"type":["null","string"]},"Path2":{"type":["null","string"]},"AdLabels":{"type":["null","string"]},"CustomerId":{"type":["null","string"]},"CustomerName":{"type":["null","string"]},"CampaignType":{"type":["null","string"]},"BaseCampaignId":{"type":["null","string"]},"AllConversions":{"type":["null","string"]},"AllRevenue":{"type":["null","string"]},"AllConversionRate":{"type":["null","string"]},"AllCostPerConversion":{"type":["null","string"]},"AllReturnOnAdSpend":{"type":["null","string"]},"AllRevenuePerConversion":{"type":["null","string"]},"FinalUrlSuffix":{"type":["null","string"]},"ViewThroughConversions":{"type":["null","string"]},"Goal":{"type":["null","string"]},"GoalType":{"type":["null","string"]},"AbsoluteTopImpressionRatePercent":{"type":["null","string"]},"TopImpressionRatePercent":{"type":["null","string"]},"_sdc_report_datetime":{"type":"string","format":"date-time"}},"additionalProperties":false,"type":"object"},"key_properties":[]}'

# Bing Ads age_gender_audience_report

bing_ads_age_gender_audience_report = '{"type":"SCHEMA","stream":"age_gender_audience_report","schema":{"properties":{"AccountName":{"type":["null","string"]},"AccountNumber":{"type":["null","string"]},"AccountId":{"type":["null","integer"]},"TimePeriod":{"type":["null","string"],"format":"date-time"},"CampaignName":{"type":["null","string"]},"CampaignId":{"type":["null","integer"]},"AdGroupName":{"type":["null","string"]},"AdGroupId":{"type":["null","integer"]},"AdDistribution":{"type":["null","string"]},"AgeGroup":{"type":["null","string"]},"Gender":{"type":["null","string"]},"Impressions":{"type":["null","integer"]},"Clicks":{"type":["null","integer"]},"Conversions":{"type":["null","number"]},"Spend":{"type":["null","number"]},"Revenue":{"type":["null","number"]},"ExtendedCost":{"type":["null","string"]},"Assists":{"type":["null","integer"]},"Language":{"type":["null","string"]},"AccountStatus":{"type":["null","string"]},"CampaignStatus":{"type":["null","string"]},"AdGroupStatus":{"type":["null","string"]},"BaseCampaignId":{"type":["null","string"]},"AllConversions":{"type":["null","string"]},"AllRevenue":{"type":["null","string"]},"ViewThroughConversions":{"type":["null","string"]},"Goal":{"type":["null","string"]},"GoalType":{"type":["null","string"]},"AbsoluteTopImpressionRatePercent":{"type":["null","string"]},"TopImpressionRatePercent":{"type":["null","string"]},"_sdc_report_datetime":{"type":"string","format":"date-time"}},"additionalProperties":false,"type":"object"},"key_properties":[]}'

# Bing Ads audience_performance_report

bing_ads_audience_performance_report = '{"type":"SCHEMA","stream":"audience_performance_report","schema":{"properties":{"AccountName":{"type":["null","string"]},"AccountNumber":{"type":["null","string"]},"AccountId":{"type":["null","integer"]},"TimePeriod":{"type":["null","string"],"format":"date-time"},"CampaignName":{"type":["null","string"]},"CampaignId":{"type":["null","integer"]},"AdGroupName":{"type":["null","string"]},"AdGroupId":{"type":["null","integer"]},"AudienceId":{"type":["null","string"]},"AudienceName":{"type":["null","string"]},"AssociationStatus":{"type":["null","string"]},"BidAdjustment":{"type":["null","string"]},"TargetingSetting":{"type":["null","string"]},"Impressions":{"type":["null","integer"]},"Clicks":{"type":["null","integer"]},"Ctr":{"type":["null","number"]},"AverageCpc":{"type":["null","number"]},"Spend":{"type":["null","number"]},"AveragePosition":{"type":["null","number"]},"Conversions":{"type":["null","number"]},"ConversionRate":{"type":["null","number"]},"CostPerConversion":{"type":["null","number"]},"Revenue":{"type":["null","number"]},"ReturnOnAdSpend":{"type":["null","number"]},"RevenuePerConversion":{"type":["null","number"]},"AccountStatus":{"type":["null","string"]},"CampaignStatus":{"type":["null","string"]},"AdGroupStatus":{"type":["null","string"]},"AudienceType":{"type":["null","string"]},"BaseCampaignId":{"type":["null","string"]},"AllConversions":{"type":["null","string"]},"AllRevenue":{"type":["null","string"]},"AllConversionRate":{"type":["null","string"]},"AllCostPerConversion":{"type":["null","string"]},"AllReturnOnAdSpend":{"type":["null","string"]},"AllRevenuePerConversion":{"type":["null","string"]},"AssociationId":{"type":["null","string"]},"AssociationLevel":{"type":["null","string"]},"ViewThroughConversions":{"type":["null","string"]},"Goal":{"type":["null","string"]},"GoalType":{"type":["null","string"]},"AbsoluteTopImpressionRatePercent":{"type":["null","string"]},"TopImpressionRatePercent":{"type":["null","string"]},"_sdc_report_datetime":{"type":"string","format":"date-time"}},"additionalProperties":false,"type":"object"},"key_properties":[]}'

# Bing Ads campaign_performance_report

bing_ads_campaign_performance_report = '{"type":"SCHEMA","stream":"campaign_performance_report","schema":{"properties":{"AccountName":{"type":["null","string"]},"AccountNumber":{"type":["null","string"]},"AccountId":{"type":["null","integer"]},"TimePeriod":{"type":["null","string"],"format":"date-time"},"CampaignStatus":{"type":["null","string"]},"CampaignName":{"type":["null","string"]},"CampaignId":{"type":["null","integer"]},"CurrencyCode":{"type":["null","string"]},"AdDistribution":{"type":["null","string"]},"Impressions":{"type":["null","integer"]},"Clicks":{"type":["null","integer"]},"Ctr":{"type":["null","number"]},"AverageCpc":{"type":["null","number"]},"Spend":{"type":["null","number"]},"AveragePosition":{"type":["null","number"]},"Conversions":{"type":["null","number"]},"ConversionRate":{"type":["null","number"]},"CostPerConversion":{"type":["null","number"]},"LowQualityClicks":{"type":["null","integer"]},"LowQualityClicksPercent":{"type":["null","number"]},"LowQualityImpressions":{"type":["null","integer"]},"LowQualityImpressionsPercent":{"type":["null","number"]},"LowQualityConversions":{"type":["null","integer"]},"LowQualityConversionRate":{"type":["null","number"]},"DeviceType":{"type":["null","string"]},"DeviceOS":{"type":["null","string"]},"ImpressionSharePercent":{"type":["null","number"]},"ImpressionLostToBudgetPercent":{"type":["null","number"]},"ImpressionLostToRankAggPercent":{"type":["null","string"]},"QualityScore":{"type":["null","number"]},"ExpectedCtr":{"type":["null","number"]},"AdRelevance":{"type":["null","number"]},"LandingPageExperience":{"type":["null","number"]},"HistoricalQualityScore":{"type":["null","string"]},"HistoricalExpectedCtr":{"type":["null","string"]},"HistoricalAdRelevance":{"type":["null","string"]},"HistoricalLandingPageExperience":{"type":["null","string"]},"PhoneImpressions":{"type":["null","integer"]},"PhoneCalls":{"type":["null","integer"]},"Ptr":{"type":["null","number"]},"Network":{"type":["null","string"]},"TopVsOther":{"type":["null","string"]},"BidMatchType":{"type":["null","string"]},"DeliveredMatchType":{"type":["null","string"]},"Assists":{"type":["null","integer"]},"Revenue":{"type":["null","number"]},"ReturnOnAdSpend":{"type":["null","number"]},"CostPerAssist":{"type":["null","number"]},"RevenuePerConversion":{"type":["null","number"]},"RevenuePerAssist":{"type":["null","number"]},"TrackingTemplate":{"type":["null","string"]},"CustomParameters":{"type":["null","string"]},"AccountStatus":{"type":["null","string"]},"BudgetName":{"type":["null","string"]},"BudgetStatus":{"type":["null","string"]},"BudgetAssociationStatus":{"type":["null","string"]},"LowQualityGeneralClicks":{"type":["null","integer"]},"LowQualitySophisticatedClicks":{"type":["null","integer"]},"CampaignLabels":{"type":["null","string"]},"ExactMatchImpressionSharePercent":{"type":["null","number"]},"CustomerId":{"type":["null","string"]},"CustomerName":{"type":["null","string"]},"ClickSharePercent":{"type":["null","string"]},"AbsoluteTopImpressionSharePercent":{"type":["null","string"]},"FinalUrlSuffix":{"type":["null","string"]},"CampaignType":{"type":["null","string"]},"TopImpressionShareLostToRankPercent":{"type":["null","string"]},"TopImpressionShareLostToBudgetPercent":{"type":["null","string"]},"AbsoluteTopImpressionShareLostToRankPercent":{"type":["null","string"]},"AbsoluteTopImpressionShareLostToBudgetPercent":{"type":["null","string"]},"TopImpressionSharePercent":{"type":["null","string"]},"AbsoluteTopImpressionRatePercent":{"type":["null","string"]},"TopImpressionRatePercent":{"type":["null","string"]},"BaseCampaignId":{"type":["null","string"]},"AllConversions":{"type":["null","string"]},"AllRevenue":{"type":["null","string"]},"AllConversionRate":{"type":["null","string"]},"AllCostPerConversion":{"type":["null","string"]},"AllReturnOnAdSpend":{"type":["null","string"]},"AllRevenuePerConversion":{"type":["null","string"]},"ViewThroughConversions":{"type":["null","string"]},"Goal":{"type":["null","string"]},"GoalType":{"type":["null","string"]},"AudienceImpressionSharePercent":{"type":["null","string"]},"AudienceImpressionLostToRankPercent":{"type":["null","string"]},"AudienceImpressionLostToBudgetPercent":{"type":["null","string"]},"RelativeCtr":{"type":["null","string"]},"_sdc_report_datetime":{"type":"string","format":"date-time"}},"additionalProperties":false,"type":"object"},"key_properties":[]}'

# Bing Ads geographic_performance_report

bing_ads_geographic_performance_report = '{"type":"SCHEMA","stream":"geographic_performance_report","schema":{"properties":{"AccountName":{"type":["null","string"]},"AccountNumber":{"type":["null","string"]},"AccountId":{"type":["null","integer"]},"TimePeriod":{"type":["null","string"],"format":"date-time"},"CampaignName":{"type":["null","string"]},"CampaignId":{"type":["null","integer"]},"AdGroupName":{"type":["null","string"]},"AdGroupId":{"type":["null","integer"]},"Country":{"type":["null","string"]},"State":{"type":["null","string"]},"MetroArea":{"type":["null","string"]},"City":{"type":["null","string"]},"CurrencyCode":{"type":["null","string"]},"AdDistribution":{"type":["null","string"]},"Impressions":{"type":["null","integer"]},"Clicks":{"type":["null","integer"]},"Ctr":{"type":["null","number"]},"AverageCpc":{"type":["null","number"]},"Spend":{"type":["null","number"]},"AveragePosition":{"type":["null","number"]},"ProximityTargetLocation":{"type":["null","string"]},"Radius":{"type":["null","number"]},"Language":{"type":["null","string"]},"BidMatchType":{"type":["null","string"]},"DeliveredMatchType":{"type":["null","string"]},"Network":{"type":["null","string"]},"TopVsOther":{"type":["null","string"]},"DeviceType":{"type":["null","string"]},"DeviceOS":{"type":["null","string"]},"Assists":{"type":["null","integer"]},"Conversions":{"type":["null","number"]},"ConversionRate":{"type":["null","number"]},"Revenue":{"type":["null","number"]},"ReturnOnAdSpend":{"type":["null","number"]},"CostPerConversion":{"type":["null","number"]},"CostPerAssist":{"type":["null","number"]},"RevenuePerConversion":{"type":["null","number"]},"RevenuePerAssist":{"type":["null","number"]},"LocationType":{"type":["null","string"]},"MostSpecificLocation":{"type":["null","string"]},"AccountStatus":{"type":["null","string"]},"CampaignStatus":{"type":["null","string"]},"AdGroupStatus":{"type":["null","string"]},"County":{"type":["null","string"]},"PostalCode":{"type":["null","string"]},"LocationId":{"type":["null","integer"]},"BaseCampaignId":{"type":["null","string"]},"AllConversions":{"type":["null","string"]},"AllRevenue":{"type":["null","string"]},"AllConversionRate":{"type":["null","string"]},"AllCostPerConversion":{"type":["null","string"]},"AllReturnOnAdSpend":{"type":["null","string"]},"AllRevenuePerConversion":{"type":["null","string"]},"ViewThroughConversions":{"type":["null","string"]},"Goal":{"type":["null","string"]},"GoalType":{"type":["null","string"]},"AbsoluteTopImpressionRatePercent":{"type":["null","string"]},"TopImpressionRatePercent":{"type":["null","string"]},"_sdc_report_datetime":{"type":"string","format":"date-time"}},"additionalProperties":false,"type":"object"},"key_properties":[]}'

# Bing Ads goals_and_funnels_report

bing_ads_goals_and_funnels_report = '{"type":"SCHEMA","stream":"goals_and_funnels_report","schema":{"properties":{"AccountName":{"type":["null","string"]},"AccountNumber":{"type":["null","string"]},"AccountId":{"type":["null","integer"]},"TimePeriod":{"type":["null","string"],"format":"date-time"},"CampaignName":{"type":["null","string"]},"CampaignId":{"type":["null","integer"]},"AdGroupName":{"type":["null","string"]},"AdGroupId":{"type":["null","integer"]},"Keyword":{"type":["null","string"]},"KeywordId":{"type":["null","integer"]},"Goal":{"type":["null","string"]},"AllConversions":{"type":["null","string"]},"Assists":{"type":["null","integer"]},"AllRevenue":{"type":["null","string"]},"GoalId":{"type":["null","integer"]},"DeviceType":{"type":["null","string"]},"DeviceOS":{"type":["null","string"]},"AccountStatus":{"type":["null","string"]},"CampaignStatus":{"type":["null","string"]},"AdGroupStatus":{"type":["null","string"]},"KeywordStatus":{"type":["null","string"]},"GoalType":{"type":["null","string"]},"ViewThroughConversions":{"type":["null","string"]},"_sdc_report_datetime":{"type":"string","format":"date-time"}},"additionalProperties":false,"type":"object"},"key_properties":[]}'

# Bing Ads keyword_performance_report

bing_ads_keyword_performance_report = '{"type":"SCHEMA","stream":"keyword_performance_report","schema":{"properties":{"AccountName":{"type":["null","string"]},"AccountNumber":{"type":["null","string"]},"AccountId":{"type":["null","integer"]},"TimePeriod":{"type":["null","string"],"format":"date-time"},"CampaignName":{"type":["null","string"]},"CampaignId":{"type":["null","integer"]},"AdGroupName":{"type":["null","string"]},"AdGroupId":{"type":["null","integer"]},"Keyword":{"type":["null","string"]},"KeywordId":{"type":["null","integer"]},"AdId":{"type":["null","integer"]},"AdType":{"type":["null","string"]},"DestinationUrl":{"type":["null","string"]},"CurrentMaxCpc":{"type":["null","number"]},"CurrencyCode":{"type":["null","string"]},"DeliveredMatchType":{"type":["null","string"]},"AdDistribution":{"type":["null","string"]},"Impressions":{"type":["null","integer"]},"Clicks":{"type":["null","integer"]},"Ctr":{"type":["null","number"]},"AverageCpc":{"type":["null","number"]},"Spend":{"type":["null","number"]},"AveragePosition":{"type":["null","number"]},"Conversions":{"type":["null","number"]},"ConversionRate":{"type":["null","number"]},"CostPerConversion":{"type":["null","number"]},"BidMatchType":{"type":["null","string"]},"DeviceType":{"type":["null","string"]},"QualityScore":{"type":["null","number"]},"ExpectedCtr":{"type":["null","number"]},"AdRelevance":{"type":["null","number"]},"LandingPageExperience":{"type":["null","number"]},"Language":{"type":["null","string"]},"HistoricalQualityScore":{"type":["null","string"]},"HistoricalExpectedCtr":{"type":["null","string"]},"HistoricalAdRelevance":{"type":["null","string"]},"HistoricalLandingPageExperience":{"type":["null","string"]},"QualityImpact":{"type":["null","number"]},"CampaignStatus":{"type":["null","string"]},"AccountStatus":{"type":["null","string"]},"AdGroupStatus":{"type":["null","string"]},"KeywordStatus":{"type":["null","string"]},"Network":{"type":["null","string"]},"TopVsOther":{"type":["null","string"]},"DeviceOS":{"type":["null","string"]},"Assists":{"type":["null","integer"]},"Revenue":{"type":["null","number"]},"ReturnOnAdSpend":{"type":["null","number"]},"CostPerAssist":{"type":["null","number"]},"RevenuePerConversion":{"type":["null","number"]},"RevenuePerAssist":{"type":["null","number"]},"TrackingTemplate":{"type":["null","string"]},"CustomParameters":{"type":["null","string"]},"FinalUrl":{"type":["null","string"]},"FinalMobileUrl":{"type":["null","string"]},"FinalAppUrl":{"type":["null","string"]},"BidStrategyType":{"type":["null","string"]},"KeywordLabels":{"type":["null","string"]},"Mainline1Bid":{"type":["null","number"]},"MainlineBid":{"type":["null","number"]},"FirstPageBid":{"type":["null","string"]},"FinalUrlSuffix":{"type":["null","string"]},"BaseCampaignId":{"type":["null","string"]},"AllConversions":{"type":["null","string"]},"AllRevenue":{"type":["null","string"]},"AllConversionRate":{"type":["null","string"]},"AllCostPerConversion":{"type":["null","string"]},"AllReturnOnAdSpend":{"type":["null","string"]},"AllRevenuePerConversion":{"type":["null","string"]},"ViewThroughConversions":{"type":["null","string"]},"Goal":{"type":["null","string"]},"GoalType":{"type":["null","string"]},"AbsoluteTopImpressionRatePercent":{"type":["null","string"]},"TopImpressionRatePercent":{"type":["null","string"]},"_sdc_report_datetime":{"type":"string","format":"date-time"}},"additionalProperties":false,"type":"object"},"key_properties":[]}'

# Bing Ads search_query_performance_report

bing_ads_search_query_performance_report = '{"type":"SCHEMA","stream":"search_query_performance_report","schema":{"properties":{"AccountName":{"type":["null","string"]},"AccountNumber":{"type":["null","string"]},"AccountId":{"type":["null","integer"]},"TimePeriod":{"type":["null","string"],"format":"date-time"},"CampaignName":{"type":["null","string"]},"CampaignId":{"type":["null","integer"]},"AdGroupName":{"type":["null","string"]},"AdGroupId":{"type":["null","integer"]},"AdId":{"type":["null","integer"]},"AdType":{"type":["null","string"]},"DestinationUrl":{"type":["null","string"]},"BidMatchType":{"type":["null","string"]},"DeliveredMatchType":{"type":["null","string"]},"CampaignStatus":{"type":["null","string"]},"AdStatus":{"type":["null","string"]},"Impressions":{"type":["null","integer"]},"Clicks":{"type":["null","integer"]},"Ctr":{"type":["null","number"]},"AverageCpc":{"type":["null","number"]},"Spend":{"type":["null","number"]},"AveragePosition":{"type":["null","number"]},"SearchQuery":{"type":["null","string"]},"Keyword":{"type":["null","string"]},"AdGroupCriterionId":{"type":["null","integer"]},"Conversions":{"type":["null","number"]},"ConversionRate":{"type":["null","number"]},"CostPerConversion":{"type":["null","number"]},"Language":{"type":["null","string"]},"KeywordId":{"type":["null","integer"]},"Network":{"type":["null","string"]},"TopVsOther":{"type":["null","string"]},"DeviceType":{"type":["null","string"]},"DeviceOS":{"type":["null","string"]},"Assists":{"type":["null","integer"]},"Revenue":{"type":["null","number"]},"ReturnOnAdSpend":{"type":["null","number"]},"CostPerAssist":{"type":["null","number"]},"RevenuePerConversion":{"type":["null","number"]},"RevenuePerAssist":{"type":["null","number"]},"AccountStatus":{"type":["null","string"]},"AdGroupStatus":{"type":["null","string"]},"KeywordStatus":{"type":["null","string"]},"CampaignType":{"type":["null","string"]},"CustomerId":{"type":["null","string"]},"CustomerName":{"type":["null","string"]},"AllConversions":{"type":["null","string"]},"AllRevenue":{"type":["null","string"]},"AllConversionRate":{"type":["null","string"]},"AllCostPerConversion":{"type":["null","string"]},"AllReturnOnAdSpend":{"type":["null","string"]},"AllRevenuePerConversion":{"type":["null","string"]},"Goal":{"type":["null","string"]},"GoalType":{"type":["null","string"]},"AbsoluteTopImpressionRatePercent":{"type":["null","string"]},"TopImpressionRatePercent":{"type":["null","string"]},"_sdc_report_datetime":{"type":"string","format":"date-time"}},"additionalProperties":false,"type":"object"},"key_properties":[]}'

recharge_addresses = """{
    
    "type": "SCHEMA",
  "stream": "addresses",
    
    "key_properties": [
        "id"
    ],
    "schema": {
        "properties": {
            "address1": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "address2": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "cart_attributes": {
                "anyOf": [
                    {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "name": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "value": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    {
                        "type": "null"
                    }
                ]
            },
            "cart_note": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "city": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "company": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "country": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "created_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "customer_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "discount_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "first_name": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "last_name": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "note_attributes": {
                "anyOf": [
                    {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "name": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "value": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    {
                        "type": "null"
                    }
                ]
            },
            "original_shipping_lines": {
                "anyOf": [
                    {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "code": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "price": {
                                    "type": [
                                        "null",
                                        "number"
                                    ]
                                },
                                "title": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    {
                        "type": "null"
                    }
                ]
            },
            "phone": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "province": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "shipping_lines_override": {
                "anyOf": [
                    {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "code": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "price": {
                                    "type": [
                                        "null",
                                        "number"
                                    ]
                                },
                                "title": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    {
                        "type": "null"
                    }
                ]
            },
            "updated_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "zip": {
                "type": [
                    "null",
                    "string"
                ]
            }
        },
        "type": "object",
        "additionalProperties": false
    },
    "stream": "addresses",
    "metadata": [
        {
            "breadcrumb": [],
            "metadata": {
                "table-key-properties": [
                    "id"
                ],
                "forced-replication-method": "INCREMENTAL",
                "valid-replication-keys": [
                    "updated_at"
                ],
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "address1"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "address2"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "cart_attributes"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "cart_note"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "city"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "company"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "country"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "created_at"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "customer_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "discount_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "first_name"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "id"
            ],
            "metadata": {
                "inclusion": "automatic"
            }
        },
        {
            "breadcrumb": [
                "properties",
                "last_name"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "note_attributes"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "original_shipping_lines"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "phone"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "province"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shipping_lines_override"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "updated_at"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "zip"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        }
    ]
}"""


recharge_charges = """ {

    "type": "SCHEMA",
    "stream": "charges",
    "key_properties": [
        "id"
    ],
    "schema": {
        "properties": {
            "address_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "billing_address": {
                "properties": {
                    "address1": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "address2": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "city": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "company": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "country": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "first_name": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "last_name": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "phone": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "province": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "zip": {
                        "type": [
                            "null",
                            "string"
                        ]
                    }
                },
                "type": [
                    "null",
                    "object"
                ],
                "additionalProperties": false
            },
            "browser_ip": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "client_details": {
                "properties": {
                    "browser_ip": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "user_agent": {
                        "type": [
                            "null",
                            "string"
                        ]
                    }
                },
                "type": [
                    "null",
                    "object"
                ],
                "additionalProperties": false
            },
            "created_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "customer_hash": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "customer_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "discount_codes": {
                "anyOf": [
                    {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "amount": {
                                    "type": [
                                        "null",
                                        "number"
                                    ]
                                },
                                "code": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "type": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    {
                        "type": "null"
                    }
                ]
            },
            "email": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "first_name": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "has_uncommited_changes": {
                "type": [
                    "null",
                    "boolean"
                ]
            },
            "id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "last_name": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "line_items": {
                "anyOf": [
                    {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "grams": {
                                    "type": [
                                        "null",
                                        "integer"
                                    ]
                                },
                                "images": {
                                    "type": [
                                        "null",
                                        "object"
                                    ],
                                    "additionalProperties": false,
                                    "properties": {
                                        "large": {
                                            "type": [
                                                "null",
                                                "string"
                                            ]
                                        },
                                        "medium": {
                                            "type": [
                                                "null",
                                                "string"
                                            ]
                                        },
                                        "original": {
                                            "type": [
                                                "null",
                                                "string"
                                            ]
                                        },
                                        "small": {
                                            "type": [
                                                "null",
                                                "string"
                                            ]
                                        }
                                    }
                                },
                                "price": {
                                    "type": [
                                        "null",
                                        "number"
                                    ]
                                },
                                "properties": {
                                    "anyOf": [
                                        {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "additionalProperties": false,
                                                "properties": {
                                                    "name": {
                                                        "type": [
                                                            "null",
                                                            "string"
                                                        ]
                                                    },
                                                    "value": {
                                                        "type": [
                                                            "null",
                                                            "string"
                                                        ]
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "type": "null"
                                        }
                                    ]
                                },
                                "quantity": {
                                    "type": [
                                        "null",
                                        "integer"
                                    ]
                                },
                                "shopify_product_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "shopify_variant_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "sku": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "subscription_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "title": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "variant_title": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "vendor": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    {
                        "type": "null"
                    }
                ]
            },
            "note": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "note_attributes": {
                "anyOf": [
                    {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "name": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "value": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    {
                        "type": "null"
                    }
                ]
            },
            "processed_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "processor_name": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "scheduled_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "shipments_count": {
                "type": [
                    "null",
                    "integer"
                ]
            },
            "shipping_address": {
                "properties": {
                    "address1": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "address2": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "city": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "company": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "country": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "first_name": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "last_name": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "phone": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "province": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "zip": {
                        "type": [
                            "null",
                            "string"
                        ]
                    }
                },
                "type": [
                    "null",
                    "object"
                ],
                "additionalProperties": false
            },
            "shipping_lines": {
                "anyOf": [
                    {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "code": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "price": {
                                    "type": [
                                        "null",
                                        "number"
                                    ]
                                },
                                "title": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    {
                        "type": "null"
                    }
                ]
            },
            "shopify_order_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "status": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "sub_total": {
                "type": [
                    "null",
                    "number"
                ]
            },
            "subtotal_price": {
                "type": [
                    "null",
                    "number"
                ]
            },
            "tags": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "tax_lines": {
                "multipleOf": 1e-08,
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_discounts": {
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_line_items_price": {
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_price": {
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_refunds": {
                "multipleOf": 1e-08,
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_tax": {
                "multipleOf": 1e-08,
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_weight": {
                "type": [
                    "null",
                    "integer"
                ]
            },
            "transaction_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "type": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "updated_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            }
        },
        "type": "object",
        "additionalProperties": false
    },
    "stream": "charges",
    "metadata": [
        {
            "breadcrumb": [],
            "metadata": {
                "table-key-properties": [
                    "id"
                ],
                "forced-replication-method": "INCREMENTAL",
                "valid-replication-keys": [
                    "updated_at"
                ],
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "address_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "billing_address"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "browser_ip"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "client_details"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "created_at"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "customer_hash"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "customer_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "discount_codes"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "email"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "first_name"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "has_uncommited_changes"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "id"
            ],
            "metadata": {
                "inclusion": "automatic"
            }
        },
        {
            "breadcrumb": [
                "properties",
                "last_name"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "line_items"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "note"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "note_attributes"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "processed_at"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "processor_name"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "scheduled_at"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shipments_count"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shipping_address"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shipping_lines"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shopify_order_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "status"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "sub_total"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "subtotal_price"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "tags"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "tax_lines"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "total_discounts"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "total_line_items_price"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "total_price"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "total_refunds"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "total_tax"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "total_weight"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "transaction_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "type"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "updated_at"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        }
    ]
}"""


recharge_orders = """{

    "type": "SCHEMA",
  "stream": "orders",

    "key_properties": [
        "id"
    ],
    "schema": {
        "properties": {
            "address_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "address_is_active": {
                "type": [
                    "null",
                    "boolean"
                ]
            },
            "billing_address": {
                "properties": {
                    "address1": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "address2": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "city": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "company": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "country": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "first_name": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "last_name": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "phone": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "province": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "zip": {
                        "type": [
                            "null",
                            "string"
                        ]
                    }
                },
                "type": [
                    "null",
                    "object"
                ],
                "additionalProperties": false
            },
            "charge_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "charge_status": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "created_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "customer_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "discount_codes": {
                "anyOf": [
                    {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "amount": {
                                    "type": [
                                        "null",
                                        "number"
                                    ]
                                },
                                "code": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "type": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    {
                        "type": "null"
                    }
                ]
            },
            "email": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "first_name": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "hash": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "is_prepaid": {
                "type": [
                    "null",
                    "boolean"
                ]
            },
            "last_name": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "line_items": {
                "anyOf": [
                    {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "grams": {
                                    "type": [
                                        "null",
                                        "integer"
                                    ]
                                },
                                "images": {
                                    "type": [
                                        "null",
                                        "object"
                                    ],
                                    "additionalProperties": false,
                                    "properties": {
                                        "large": {
                                            "type": [
                                                "null",
                                                "string"
                                            ]
                                        },
                                        "medium": {
                                            "type": [
                                                "null",
                                                "string"
                                            ]
                                        },
                                        "original": {
                                            "type": [
                                                "null",
                                                "string"
                                            ]
                                        },
                                        "small": {
                                            "type": [
                                                "null",
                                                "string"
                                            ]
                                        }
                                    }
                                },
                                "price": {
                                    "type": [
                                        "null",
                                        "number"
                                    ],
                                    "multipleOf": 1e-08
                                },
                                "properties": {
                                    "anyOf": [
                                        {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "additionalProperties": false,
                                                "properties": {
                                                    "name": {
                                                        "type": [
                                                            "null",
                                                            "string"
                                                        ]
                                                    },
                                                    "value": {
                                                        "type": [
                                                            "null",
                                                            "string"
                                                        ]
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            "type": "null"
                                        }
                                    ]
                                },
                                "quantity": {
                                    "type": [
                                        "null",
                                        "integer"
                                    ]
                                },
                                "shopify_product_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "shopify_variant_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "sku": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "subscription_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "title": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "variant_title": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "vendor": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    {
                        "type": "null"
                    }
                ]
            },
            "note": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "note_attributes": {
                "anyOf": [
                    {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "name": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "value": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    {
                        "type": "null"
                    }
                ]
            },
            "payment_processor": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "processed_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "scheduled_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "shipped_date": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "shipping_address": {
                "properties": {
                    "address1": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "address2": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "city": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "company": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "country": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "first_name": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "last_name": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "phone": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "province": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "zip": {
                        "type": [
                            "null",
                            "string"
                        ]
                    }
                },
                "type": [
                    "null",
                    "object"
                ],
                "additionalProperties": false
            },
            "shipping_date": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            },
            "shipping_lines": {
                "anyOf": [
                    {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "code": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "price": {
                                    "type": [
                                        "null",
                                        "number"
                                    ]
                                },
                                "title": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    {
                        "type": "null"
                    }
                ]
            },
            "shopify_cart_token": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "shopify_customer_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "shopify_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "shopify_order_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "shopify_order_number": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "status": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "subtotal_price": {
                "type": [
                    "null",
                    "number"
                ]
            },
            "tags": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "tax_lines": {
                "anyOf": [
                    {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "code": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "price": {
                                    "type": [
                                        "null",
                                        "number"
                                    ]
                                },
                                "title": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    {
                        "type": "null"
                    }
                ]
            },
            "total_discounts": {
                "multipleOf": 1e-08,
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_line_items_price": {
                "multipleOf": 1e-08,
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_price": {
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_refunds": {
                "multipleOf": 1e-08,
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_tax": {
                "multipleOf": 1e-08,
                "type": [
                    "null",
                    "number"
                ]
            },
            "total_weight": {
                "type": [
                    "null",
                    "integer"
                ]
            },
            "transaction_id": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "type": {
                "type": [
                    "null",
                    "string"
                ]
            },
            "updated_at": {
                "format": "date-time",
                "type": [
                    "null",
                    "string"
                ]
            }
        },
        "type": "object",
        "additionalProperties": false
    },
    "stream": "orders",
    "metadata": [
        {
            "breadcrumb": [],
            "metadata": {
                "table-key-properties": [
                    "id"
                ],
                "forced-replication-method": "INCREMENTAL",
                "valid-replication-keys": [
                    "updated_at"
                ],
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "address_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "address_is_active"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "billing_address"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "charge_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "charge_status"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "created_at"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "customer_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "discount_codes"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "email"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "first_name"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "hash"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "id"
            ],
            "metadata": {
                "inclusion": "automatic"
            }
        },
        {
            "breadcrumb": [
                "properties",
                "is_prepaid"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "last_name"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "line_items"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "note"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "note_attributes"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "payment_processor"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "processed_at"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "scheduled_at"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shipped_date"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shipping_address"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shipping_date"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shipping_lines"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shopify_cart_token"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shopify_customer_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shopify_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shopify_order_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "shopify_order_number"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "status"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "subtotal_price"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "tags"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "tax_lines"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "total_discounts"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "total_line_items_price"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "total_price"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "total_refunds"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "total_tax"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "total_weight"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "transaction_id"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "type"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        },
        {
            "breadcrumb": [
                "properties",
                "updated_at"
            ],
            "metadata": {
                "inclusion": "available",
                "selected": true
            }
        }
    ]
}"""



HubSpot_contact_lists_schema_original = """{
    "streams": [
        {
            "stream": "contact_lists",
            "tap_stream_id": "contact_lists",
            "schema": {
                "type": "object",
                "properties": {
                    "portalId": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "listId": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "internalListId": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "createdAt": {
                        "type": [
                            "null",
                            "string"
                        ],
                        "format": "date-time"
                    },
                    "updatedAt": {
                        "type": [
                            "null",
                            "string"
                        ],
                        "format": "date-time"
                    },
                    "name": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "listType": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "parentId": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "authorId": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "filters": {
                        "type": [
                            "null",
                            "array"
                        ],
                        "items": {
                            "type": [
                                "null",
                                "array"
                            ],
                            "items": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "withinTimeMode": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "filterFamily": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "operator": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "type": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "property": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "value": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "checkPastVersions": {
                                        "type": [
                                            "null",
                                            "boolean"
                                        ]
                                    }
                                }
                            }
                        }
                    },
                    "metaData": {
                        "type": [
                            "null",
                            "object"
                        ],
                        "properties": {
                            "size": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "lastSizeChangeAt": {
                                "type": [
                                    "null",
                                    "string"
                                ],
                                "format": "date-time"
                            },
                            "processing": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "lastProcessingStateChangeAt": {
                                "type": [
                                    "null",
                                    "string"
                                ],
                                "format": "date-time"
                            },
                            "error": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "listReferencesCount": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "parentFolderId": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            }
                        }
                    },
                    "archived": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "dynamic": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "readOnly": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "limitExempt": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "deleteable": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    }
                }
            },
            "metadata": [
                {
                    "breadcrumb": [],
                    "metadata": {
                        "table-key-properties": [
                            "listId"
                        ],
                        "forced-replication-method": "INCREMENTAL",
                        "valid-replication-keys": [
                            "updatedAt"
                        ],
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "portalId"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "listId"
                    ],
                    "metadata": {
                        "inclusion": "automatic"
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "internalListId"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "createdAt"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "updatedAt"
                    ],
                    "metadata": {
                        "inclusion": "automatic"
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "name"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "listType"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "parentId"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "authorId"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "filters"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "metaData"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "archived"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "dynamic"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "readOnly"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "limitExempt"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "deleteable"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                }
            ]
        }
    ]
}"""

# extracted stream schema
# added key_properties, and type key-value pair
HubSpot_contact_lists_schema_fixed_test = """{

            "type": "SCHEMA",
            "stream": "contact_lists",

            "key_properties": [
                "listId"
            ],

            "schema": {
                "type": "object",
                "properties": {
                    "portalId": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "listId": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "internalListId": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "createdAt": {
                        "type": [
                            "null",
                            "string"
                        ],
                        "format": "date-time"
                    },
                    "updatedAt": {
                        "type": [
                            "null",
                            "string"
                        ],
                        "format": "date-time"
                    },
                    "name": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "listType": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "parentId": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "authorId": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "filters": {
                        "type": [
                            "null",
                            "array"
                        ],
                        "items": {
                            "type": [
                                "null",
                                "array"
                            ],
                            "items": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "withinTimeMode": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "filterFamily": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "operator": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "type": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "property": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "value": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "checkPastVersions": {
                                        "type": [
                                            "null",
                                            "boolean"
                                        ]
                                    }
                                }
                            }
                        }
                    },
                    "metaData": {
                        "type": [
                            "null",
                            "object"
                        ],
                        "properties": {
                            "size": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "lastSizeChangeAt": {
                                "type": [
                                    "null",
                                    "string"
                                ],
                                "format": "date-time"
                            },
                            "processing": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "lastProcessingStateChangeAt": {
                                "type": [
                                    "null",
                                    "string"
                                ],
                                "format": "date-time"
                            },
                            "error": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "listReferencesCount": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "parentFolderId": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            }
                        }
                    },
                    "archived": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "dynamic": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "readOnly": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "limitExempt": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "deleteable": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    }
                }
            },
            "metadata": [
                {
                    "breadcrumb": [],
                    "metadata": {
                        "table-key-properties": [
                            "listId"
                        ],
                        "forced-replication-method": "INCREMENTAL",
                        "valid-replication-keys": [
                            "updatedAt"
                        ],
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "portalId"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "listId"
                    ],
                    "metadata": {
                        "inclusion": "automatic"
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "internalListId"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "createdAt"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "updatedAt"
                    ],
                    "metadata": {
                        "inclusion": "automatic"
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "name"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "listType"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "parentId"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "authorId"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "filters"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "metaData"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "archived"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "dynamic"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "readOnly"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "limitExempt"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                },
                {
                    "breadcrumb": [
                        "properties",
                        "deleteable"
                    ],
                    "metadata": {
                        "inclusion": "available",
                        "selected": true
                    }
                }
            ]
        }"""

