| Method | Endpoint | Input | Fields |
| --- | --- | --- | --- |
| GET | `/CreativeOne/Charging/CreatorGetBonusInfo` | none | — |
| GET | `/CreativeOne/Charging/CreatorGetEarningDetail` | params | `startTimestamp`, `endTimestamp`, `page`, `limit` |
| GET | `/CreativeOne/Charging/CreatorGetEarningSummary` | params | `startTimestamp`, `endTimestamp`, `currentTimestamp` |
| GET | `/CreativeOne/Charging/CreatorGetEarningSummaryForAnalytics` | params | `lastXMonths` |
| GET | `/CreativeOne/Charging/CreatorGetPaidDetailForBonus` | params | `transactionID` |
| GET | `/CreativeOne/Charging/CreatorGetPaidDetailForVideo` | params | `transactionID`, `page`, `limit` |
| GET | `/CreativeOne/Charging/CreatorGetPendingPaymentDetailForBonus` | none | — |
| GET | `/CreativeOne/Charging/CreatorGetPendingPaymentDetailForVideo` | params | `page`, `limit` |
| GET | `/CreativeOne/Charging/CreatorGetRewardsDetailForVideo` | params | `itemID`, `videoID` |
| GET | `/CreativeOne/Charging/CreatorGetTotalPendingPaymentPrice` | none | — |
| GET | `/CreativeOne/Charging/CreatorGetTransactionSummary` | params | `transactionID`, `settlementOrderID` |
| GET | `/CreativeOne/Charging/CreatorGetVideoAdsRevenueShareDetail` | params | `itemID`, `videoID`, `lastXDays` |
| GET | `/CreativeOne/Charging/CreatorGetVideoBonusInfo` | params | `itemID`, `videoID` |
| GET | `/CreativeOne/Charging/CreatorGetVideoEarningSummary` | params | `itemID`, `videoID` |
| POST | `/CreativeOne/Control/CreatorRiskCheck` | data | `source`, `params` |
| POST | `/CreativeOne/Creator/BatchReadInhouseNotice` | data | `noticeIDList`, `readAll` |
| GET | `/CreativeOne/Creator/CheckCreatorMediaKitAccess` | none | — |
| GET | `/CreativeOne/Creator/CheckJoinSourceAvailability` | params | `channelCode` |
| GET | `/CreativeOne/Creator/CheckPrivatePoolLinkCanBeBound` | params | `channelCode` |
| POST | `/CreativeOne/Creator/CreateAgencyUnbindingRecord` | data | `relationshipID` |
| POST | `/CreativeOne/Creator/CreateCreatorRelationship` | data | `relationshipType`, `entityType`, `entityID`, `channelCode`, `privateCreatorNote`, `privateCreatorCategories` |
| GET | `/CreativeOne/Creator/CreatorGetTTOCollabsProfile` | none | — |
| GET | `/CreativeOne/Creator/CreatorGetTTOCollabsSetting` | none | — |
| GET | `/CreativeOne/Creator/CreatorQueryTTOCollabsItemList` | params | `page`, `limit` |
| GET | `/CreativeOne/Creator/CreatorQueryTTOCollabsItemPlayData` | params | `page`, `limit` |
| POST | `/CreativeOne/Creator/CreatorRegister` | data | `protocolIDs`, `aioCode` |
| POST | `/CreativeOne/Creator/CreatorSaveTTOCollabsSetting` | data | `setting` |
| POST | `/CreativeOne/Creator/DeleteCreatorMediaKit` | data | `mediaKitID` |
| GET | `/CreativeOne/Creator/GetAgencyCooperationRecords` | params | `unbindingRecordID` |
| GET | `/CreativeOne/Creator/GetCreatorActivityItemList` | params | `page`, `limit` |
| GET | `/CreativeOne/Creator/GetCreatorAppealStatus` | params | `appealType` |
| GET | `/CreativeOne/Creator/GetCreatorBannerConfig` | params | `limit` |
| GET | `/CreativeOne/Creator/GetCreatorBenefit` | params | `benefitDescIDList` |
| GET | `/CreativeOne/Creator/GetCreatorHistoricalContact` | none | — |
| GET | `/CreativeOne/Creator/GetCreatorHistoricalRegistration` | none | — |
| GET | `/CreativeOne/Creator/GetCreatorIncentiveInfo` | none | — |
| GET | `/CreativeOne/Creator/GetCreatorMediaKitList` | params | `page`, `limit` |
| GET | `/CreativeOne/Creator/GetCreatorOrderContactInfo` | params | `contactID`, `infoType` |
| GET | `/CreativeOne/Creator/GetCreatorPortfolioList` | params | `status`, `lang` |
| GET | `/CreativeOne/Creator/GetCreatorProfileDetail` | none | — |
| GET | `/CreativeOne/Creator/GetCreatorRegisterType` | params | `groupIDs`, `campaignID`, `creatorAgencyID`, `cooperationID`, `preAuthID`, `relationshipID`, `brandLinkID`, `aioCode` |
| GET | `/CreativeOne/Creator/GetCreatorSettings` | none | — |
| GET | `/CreativeOne/Creator/GetCreatorStatsData` | none | — |
| GET | `/CreativeOne/Creator/GetDefaultMediaKit` | none | — |
| GET | `/CreativeOne/Creator/GetInhouseNoticeList` | params | `page`, `limit` |
| GET | `/CreativeOne/Creator/GetPlatformConfig` | none | — |
| GET | `/CreativeOne/Creator/GetPortfolioVideoOptionList` | params | `videoType`, `orderBy`, `page`, `limit`, `cursor` |
| GET | `/CreativeOne/Creator/GetPublicVideoInfo` | params | `videoID` |
| GET | `/CreativeOne/Creator/GetRelationshipDetail` | params | `relationshipID`, `aioClientID` |
| GET | `/CreativeOne/Creator/MGetPublicVideoInfo` | params | `videoIDList` |
| GET | `/CreativeOne/Creator/QueryCreatorRelationship` | params | `relationshipType`, `packInfoType` |
| GET | `/CreativeOne/Creator/Read/GetCreatorBaseInfo` | none | — |
| GET | `/CreativeOne/Creator/Read/PreviewGetCreatorBannerConfigList` | params | `limit` |
| GET | `/CreativeOne/Creator/Read/PreviewGetCreatorProfile` | none | — |
| POST | `/CreativeOne/Creator/Read/PreviewGetCreatorRankLatestSlot` | none | — |
| GET | `/CreativeOne/Creator/Read/PreviewGetCreatorStatsData` | none | — |
| GET | `/CreativeOne/Creator/Read/PreviewGetTopContentsList` | params | `periodDimension`, `periodEndTimestamp`, `orderByMetric`, `countryCode`, `contentLabelIDs`, `organicOnly`, `limit`, `page` |
| GET | `/CreativeOne/Creator/Read/PreviewGetTopContentsOverview` | none | — |
| POST | `/CreativeOne/Creator/Read/PreviewMGetCreatorRankList` | data | `itemList` |
| GET | `/CreativeOne/Creator/Read/PreviewMGetPublicVideoInfo` | params | `videoIDList` |
| GET | `/CreativeOne/Creator/Read/PreviewSaveCreatorFeedback` | params | `feedbackType`, `score`, `content`, `entityID`, `entityType` |
| POST | `/CreativeOne/Creator/SaveCreatorAppeal` | data | `appealType`, `appealDataList` |
| GET | `/CreativeOne/Creator/SaveCreatorFeedback` | params | `feedbackType`, `score`, `content`, `entityID`, `entityType` |
| POST | `/CreativeOne/Creator/SaveCreatorMediaKit` | data | `mediaKitInfo` |
| POST | `/CreativeOne/Creator/UpdateAgencyUnbindingRecord` | data | `unbindingRecordID`, `operation` |
| POST | `/CreativeOne/Creator/UpdateCreatorOrderContactInfo` | data | `infoType`, `infoDetail`, `contactID` |
| POST | `/CreativeOne/Creator/UpdateCreatorPortfolioList` | data | `videoList`, `actionType` |
| POST | `/CreativeOne/Creator/UpdateCreatorProfileDetail` | data | `profileTypeList`, `creatorProfile`, `isMigrate` |
| POST | `/CreativeOne/Creator/UpdateCreatorRelationship` | data | `relationshipID`, `agree` |
| POST | `/CreativeOne/Creator/UpdateCreatorSettings` | data | `settingsTypeList`, `creatorSettings` |
| POST | `/CreativeOne/Creator/UpdateCreatorShippingInfo` | data | `creatorShippingInfo`, `shippingContactID` |
| POST | `/CreativeOne/DataSpace/BrandLibrary/CreatorGetUndisclosedFlaggedItemInfos` | data | `page`, `limit` |
| GET | `/CreativeOne/MatchLabel/GetMatchLabelTreeByType` | params | `labelType`, `labelLevel`, `labelStatus`, `simpleTree`, `labelVersion` |
| POST | `/CreativeOne/MatchMaking/CreatorGetCampaignList` | data | `page`, `limit`, `reqTrackID`, `filter`, `sortType`, `scene`, `abParams` |
| POST | `/CreativeOne/MatchMaking/CreatorGetRankLatestSlot` | data | `needLoaderList`, `needLatestData`, `params` |
| POST | `/CreativeOne/MatchMaking/CreatorGetSearchList` | data | `page`, `limit`, `keyword`, `searchScene`, `searchType`, `abParams`, `chargingStatus` |
| POST | `/CreativeOne/MatchMaking/CreatorGetSearchSuggest` | data | `keyword`, `abParams`, `searchScene`, `limit` |
| POST | `/CreativeOne/MatchMaking/CreatorMGetCreatorRankList` | data | `itemList` |
| POST | `/CreativeOne/MatchPack/GetTTCreatorCard` | data | `needLoaderList`, `needLatestData`, `params` |
| POST | `/CreativeOne/OrderCommand/CreatorAcceptOpportunity` | data | `opportunityID`, `screeningAnswers`, `contactID`, `contactInfoOppoShown`, `shippingInfoID`, `negotiatePrice100K`, `proposalMessage`, `skuProductID`, `isVideoAuthorizationToggleOn` |
| POST | `/CreativeOne/OrderCommand/CreatorAnswerCheck` | data | `campaignID`, `screeningAnswers`, `opportunityID`, `partnerCampaignID` |
| POST | `/CreativeOne/OrderCommand/CreatorApplyCampaign` | data | `campaignID`, `screeningAnswers`, `contactID`, `contactInfoOppoShown`, `shippingInfoID`, `negotiatePrice100K`, `proposalMessage`, `flatFee100K`, `currency`, `skuProductID`, `isVideoAuthorizationToggleOn`, `partnerCampaignID` |
| POST | `/CreativeOne/OrderCommand/CreatorApplyMultiProducts` | data | `campaignID`, `screeningAnswers`, `contactID`, `contactInfoOppoShown`, `shippingInfoID`, `skuProductIDs`, `flatFee100K`, `currency`, `isVideoAuthorizationToggleOn` |
| POST | `/CreativeOne/OrderCommand/CreatorCancelOrder` | data | `orderID`, `cancellationReasons` |
| POST | `/CreativeOne/OrderCommand/CreatorCreateNegotiation` | data | `opportunityID`, `negotiatePrice100K`, `proposalMessage` |
| POST | `/CreativeOne/OrderCommand/CreatorExtendSubmissionDate` | data | `orderID`, `reason` |
| POST | `/CreativeOne/OrderCommand/CreatorHandleSparkAds` | data | `orderID`, `itemID`, `action` |
| POST | `/CreativeOne/OrderCommand/CreatorJoinCampaignV2` | data | `campaignID`, `joinSource`, `flatFee100K`, `currency`, `isVideoAuthorizationToggleOn`, `partnerCampaignID` |
| POST | `/CreativeOne/OrderCommand/CreatorJoinWaitList` | data | `campaignID`, `flatFee100K`, `currency`, `isVideoAuthorizationToggleOn` |
| POST | `/CreativeOne/OrderCommand/CreatorOperateContentCooperation` | data | `cooperationID`, `operation`, `authDays`, `otherRejectReason`, `rejectReason`, `promotionLink` |
| POST | `/CreativeOne/OrderCommand/CreatorPreAuthorizeContentCooperation` | data | `authDays`, `operation`, `optoutReason`, `reasonDetail` |
| POST | `/CreativeOne/OrderCommand/CreatorQuitOpportunity` | data | `opportunityID`, `cancellationReasons` |
| POST | `/CreativeOne/OrderCommand/CreatorQuitWaitList` | data | `opportunityID` |
| POST | `/CreativeOne/OrderCommand/CreatorReceiveProduct` | data | `orderID` |
| POST | `/CreativeOne/OrderCommand/CreatorRejectCampaignLinkItem` | data | `orderID` |
| POST | `/CreativeOne/OrderCommand/CreatorRejectOpportunity` | data | `opportunityID`, `reasons` |
| POST | `/CreativeOne/OrderCommand/CreatorReplyHistoricalBASparkAdsAuth` | data | `authStatus` |
| POST | `/CreativeOne/OrderCommand/CreatorReplyVideoAuthorization` | data | `orderID`, `isAccept`, `creatorAuthorizationToggleConfig` |
| POST | `/CreativeOne/OrderCommand/CreatorSubmitVideoAppeal` | data | `orderID`, `videoID`, `contentType`, `reasonList`, `appealType` |
| POST | `/CreativeOne/OrderCommand/CreatorUploadCreative` | data | `videoID`, `videoName`, `orderID`, `videoMeta` |
| POST | `/CreativeOne/OrderCommand/CreatorWithdrawCreative` | data | `orderID` |
| GET | `/CreativeOne/OrderQuery/CreatorAnalyticOrderInfo` | params | `itemID`, `videoID` |
| GET | `/CreativeOne/OrderQuery/CreatorCampaignManagementHomepage` | none | — |
| GET | `/CreativeOne/OrderQuery/CreatorCollabList` | params | `collabStage`, `limit`, `page`, `campaignID` |
| GET | `/CreativeOne/OrderQuery/CreatorGetBlastDetails` | params | `blastID` |
| GET | `/CreativeOne/OrderQuery/CreatorGetCollabDetailV2` | params | `campaignID`, `opportunityID`, `orderID`, `creatorAgencyID`, `joinSource`, `partnerCampaignID` |
| GET | `/CreativeOne/OrderQuery/CreatorGetContentCooperationDetailByTtuid` | params | `cooperationID` |
| GET | `/CreativeOne/OrderQuery/CreatorGetFileList` | params | `campaignID`, `folderID`, `orderType`, `limit`, `page` |
| GET | `/CreativeOne/OrderQuery/CreatorGetFolderTree` | params | `campaignID` |
| GET | `/CreativeOne/OrderQuery/CreatorGetGeneratedContent` | params | `campaignID`, `generateAction`, `taskID` |
| GET | `/CreativeOne/OrderQuery/CreatorGetLinkingRequestByID` | params | `linkingRequestID` |
| GET | `/CreativeOne/OrderQuery/CreatorGetOrderDetail` | params | `orderID` |
| GET | `/CreativeOne/OrderQuery/CreatorGetOrderTrackingInfo` | params | `orderID` |
| GET | `/CreativeOne/OrderQuery/CreatorGetPostItemList` | params | `page`, `limit`, `scene`, `orderID`, `brandLinkID` |
| GET | `/CreativeOne/OrderQuery/CreatorGetPreAuthorizationStatusByAioid` | none | — |
| GET | `/CreativeOne/OrderQuery/CreatorGetPreAuthorizationStatusByTtuid` | none | — |
| GET | `/CreativeOne/OrderQuery/CreatorRespondLinkingNegotiation` | params | `linkingRequestID`, `operation`, `orderID` |
| POST | `/CreativeOne/OrderQuery/CreatorSearchProductInfos` | data | `campaignID`, `catalogSkuID`, `catalogSpuID`, `productQuery`, `sortCondition`, `page`, `limit` |
| GET | `/CreativeOne/OrderQuery/GetCreatorSpot` | none | — |
| GET | `/CreativeOne/OrderQuery/GetVideoUrlByVideoIDOrItemID` | params | `videoID`, `itemID` |
| POST | `/CreativeOne/Passport/CreatorSignProtocol` | data | `protocolIDS`, `bizFrom`, `source`, `targetType`, `targetID` |
| POST | `/CreativeOne/Passport/CreatorSignProtocolByTTUID` | data | `protocolIDS`, `bizFrom`, `source`, `targetType`, `targetID` |
| GET | `/CreativeOne/Passport/GetCreatorProtocolDetailInfoByTTUID` | params | `protocolID` |
| GET | `/CreativeOne/Passport/GetCreatorProtocolsSignatureStatus` | params | `groupIDS`, `targetType`, `targetID` |
| GET | `/CreativeOne/Passport/PerLoginCheck` | params | `source`, `groupIDS`, `simpleCheck` |
| GET | `/CreativeOne/Payment/ExchangeCurrency` | params | `sourceCurrency`, `targetCurrency`, `sourceAmount100k`, `convertTimestamp`, `rateSource` |
| GET | `/CreativeOne/Payment/GetCreatorEarningDetail` | params | `transactionID`, `bizOrderID`, `routingParam` |
| GET | `/CreativeOne/Payment/GetCreatorIncomeInfo` | params | `needBalance`, `needDetail` |
| GET | `/CreativeOne/Payment/GetCreatorMonthlyAmount` | params | `cTzOffset`, `transactionType`, `transactionSource`, `startTime`, `endTime` |
| GET | `/CreativeOne/Payment/GetCreatorPaymentConfig` | params | `routingParam` |
| GET | `/CreativeOne/Payment/GetCreatorTransactionAccountURL` | none | — |
| GET | `/CreativeOne/Payment/GetCreatorTransactionList` | params | `transactionType`, `transactionSource`, `startTime`, `endTime`, `limit`, `page` |
| GET | `/CreativeOne/Payment/GetCreatorWithdrawDetail` | params | `transactionID` |
| GET | `/CreativeOne/Payment/GetCreatorWithdrawURL` | params | `cAid`, `ttLanguage`, `deviceID` |
| GET | `/CreativeOne/Report/CreatorGetTopContentsList` | params | `periodDimension`, `periodEndTimestamp`, `orderByMetric`, `countryCode`, `contentLabelIDs`, `organicOnly`, `limit`, `page` |
| GET | `/CreativeOne/Report/CreatorGetVideoPerfData` | params | `orderID`, `videoID`, `itemID` |
| GET | `/CreativeOne/Report/GetTopContentsOverview` | none | — |
