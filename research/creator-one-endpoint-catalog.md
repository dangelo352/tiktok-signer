# Complete TikTok One endpoint catalog

Source SHA-256: `98edb502a3e14afe104b6068f6b17230603c376b308fcd5eec53c8c45f5d2585`  
Official bundle: `https://sf16-website.neutral.ttwstatic.com/obj/tiktok_web_static/ad/one/creator/resource/js/creative/creatormarketplace.3968c740.js`  
Total: **564** routes — **427 UNKNOWN**, **87 GET**, **50 POST**

Safety: GET routes are read-only candidates and still require an explicit allowlist. POST and UNKNOWN routes are never called automatically.

## BrandSafety (15)

| Action | Method | Classification | Endpoint | Input | Parameters | Live |
| --- | --- | --- | --- | --- | --- | --- |
| Add keywords in the brand safety service. | UNKNOWN | unknown | `/CreativeOne/BrandSafety/AddKeywords` | unwrapped | — | Not tested |
| Create report in the brand safety service. | UNKNOWN | unknown | `/CreativeOne/BrandSafety/CreateReport` | unwrapped | — | Not tested |
| Delete keywords in the brand safety service. | UNKNOWN | unknown | `/CreativeOne/BrandSafety/DeleteKeywords` | unwrapped | — | Not tested |
| Delete report in the brand safety service. | UNKNOWN | unknown | `/CreativeOne/BrandSafety/DeleteReport` | unwrapped | — | Not tested |
| Download export in the brand safety service. | UNKNOWN | unknown | `/CreativeOne/BrandSafety/DownloadExport` | unwrapped | — | Not tested |
| Export report in the brand safety service. | UNKNOWN | unknown | `/CreativeOne/BrandSafety/ExportReport` | unwrapped | — | Not tested |
| Get creator evidence list in the brand safety service. | UNKNOWN | unknown | `/CreativeOne/BrandSafety/GetCreatorEvidenceList` | unwrapped | — | Not tested |
| Get creator video evidence detail in the brand safety service. | UNKNOWN | unknown | `/CreativeOne/BrandSafety/GetCreatorVideoEvidenceDetail` | unwrapped | — | Not tested |
| Get keyword settings in the brand safety service. | UNKNOWN | unknown | `/CreativeOne/BrandSafety/GetKeywordSettings` | unwrapped | — | Not tested |
| Get report creator check list in the brand safety service. | UNKNOWN | unknown | `/CreativeOne/BrandSafety/GetReportCreatorCheckList` | unwrapped | — | Not tested |
| Get report summary in the brand safety service. | UNKNOWN | unknown | `/CreativeOne/BrandSafety/GetReportSummary` | unwrapped | — | Not tested |
| Report risk feedback in the brand safety service. | UNKNOWN | unknown | `/CreativeOne/BrandSafety/ReportRiskFeedback` | unwrapped | — | Not tested |
| Report settings in the brand safety service. | UNKNOWN | unknown | `/CreativeOne/BrandSafety/ReportSettings` | unwrapped | — | Not tested |
| Reports in the brand safety service. | UNKNOWN | unknown | `/CreativeOne/BrandSafety/Reports` | unwrapped | — | Not tested |
| Review video status in the brand safety service. | UNKNOWN | unknown | `/CreativeOne/BrandSafety/ReviewVideoStatus` | unwrapped | — | Not tested |

## Charging (42)

| Action | Method | Classification | Endpoint | Input | Parameters | Live |
| --- | --- | --- | --- | --- | --- | --- |
| Admi get payslip global data in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/AdmiGetPayslipGlobalData` | unwrapped | — | Not tested |
| Admin confirm payslip v2 in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/AdminConfirmPayslipV2` | unwrapped | — | Not tested |
| Admin export payslip detail in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/AdminExportPayslipDetail` | unwrapped | — | Not tested |
| Admin generate compensation sheet v2 in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/AdminGenerateCompensationSheetV2` | unwrapped | — | Not tested |
| Admin get creator monthly earning in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/AdminGetCreatorMonthlyEarning` | unwrapped | — | Not tested |
| Admin get partner invoice country list in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/AdminGetPartnerInvoiceCountryList` | unwrapped | — | Not tested |
| Admin get partner invoice list in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/AdminGetPartnerInvoiceList` | unwrapped | — | Not tested |
| Admin get payment approval ticket detail in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/AdminGetPaymentApprovalTicketDetail` | unwrapped | — | Not tested |
| Admin get payment approval ticket list in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/AdminGetPaymentApprovalTicketList` | unwrapped | — | Not tested |
| Admin get payment list in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/AdminGetPaymentList` | unwrapped | — | Not tested |
| Admin get payslip by ids in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/AdminGetPayslipByIDs` | unwrapped | — | Not tested |
| Admin mark pay for partner invoice in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/AdminMarkPayForPartnerInvoice` | unwrapped | — | Not tested |
| Admin review parter invoice in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/AdminReviewParterInvoice` | unwrapped | — | Not tested |
| Admin send payment in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/AdminSendPayment` | unwrapped | — | Not tested |
| Admin update compensation from sheet v2 in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/AdminUpdateCompensationFromSheetV2` | unwrapped | — | Not tested |
| Admin update partner invoice in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/AdminUpdatePartnerInvoice` | unwrapped | — | Not tested |
| Client get special credits in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/ClientGetSpecialCredits` | unwrapped | — | Not tested |
| Client get transaction list for creator solution in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/ClientGetTransactionListForCreatorSolution` | unwrapped | — | Not tested |
| Client get transaction list for partner solution in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/ClientGetTransactionListForPartnerSolution` | unwrapped | — | Not tested |
| Creator get bonus info in the charging service. | GET | read-only | `/CreativeOne/Charging/CreatorGetBonusInfo` | none | — | Not tested |
| Creator get earning detail in the charging service. | GET | read-only | `/CreativeOne/Charging/CreatorGetEarningDetail` | params | `startTimestamp`, `endTimestamp`, `page`, `limit` | Not tested |
| Creator get earning summary in the charging service. | GET | read-only | `/CreativeOne/Charging/CreatorGetEarningSummary` | params | `startTimestamp`, `endTimestamp`, `currentTimestamp` | Not tested |
| Creator get earning summary for analytics in the charging service. | GET | read-only | `/CreativeOne/Charging/CreatorGetEarningSummaryForAnalytics` | params | `lastXMonths` | Not tested |
| Creator get paid detail for bonus in the charging service. | GET | read-only | `/CreativeOne/Charging/CreatorGetPaidDetailForBonus` | params | `transactionID` | Not tested |
| Creator get paid detail for video in the charging service. | GET | read-only | `/CreativeOne/Charging/CreatorGetPaidDetailForVideo` | params | `transactionID`, `page`, `limit` | Not tested |
| Creator get pending payment detail for bonus in the charging service. | GET | read-only | `/CreativeOne/Charging/CreatorGetPendingPaymentDetailForBonus` | none | — | Not tested |
| Creator get pending payment detail for video in the charging service. | GET | read-only | `/CreativeOne/Charging/CreatorGetPendingPaymentDetailForVideo` | params | `page`, `limit` | Not tested |
| Creator get rewards detail for video in the charging service. | GET | read-only | `/CreativeOne/Charging/CreatorGetRewardsDetailForVideo` | params | `itemID`, `videoID` | Not tested |
| Creator get total pending payment price in the charging service. | GET | read-only | `/CreativeOne/Charging/CreatorGetTotalPendingPaymentPrice` | none | — | Not tested |
| Creator get transaction summary in the charging service. | GET | read-only | `/CreativeOne/Charging/CreatorGetTransactionSummary` | params | `transactionID`, `settlementOrderID` | Not tested |
| Creator get video ads revenue share detail in the charging service. | GET | read-only | `/CreativeOne/Charging/CreatorGetVideoAdsRevenueShareDetail` | params | `itemID`, `videoID`, `lastXDays` | Not tested |
| Creator get video bonus info in the charging service. | GET | read-only | `/CreativeOne/Charging/CreatorGetVideoBonusInfo` | params | `itemID`, `videoID` | Not tested |
| Creator get video earning summary in the charging service. | GET | read-only | `/CreativeOne/Charging/CreatorGetVideoEarningSummary` | params | `itemID`, `videoID` | Not tested |
| Get refund detail in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/GetRefundDetail` | unwrapped | — | Not tested |
| Mcn get invoice list in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/MCNGetInvoiceList` | unwrapped | — | Not tested |
| Mcn get pending settlement info in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/MCNGetPendingSettlementInfo` | unwrapped | — | Not tested |
| Mcn trigger settle in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/MCNTriggerSettle` | unwrapped | — | Not tested |
| Partner get charging order list in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/PartnerGetChargingOrderList` | unwrapped | — | Not tested |
| Partner get invoice list in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/PartnerGetInvoiceList` | unwrapped | — | Not tested |
| Partner manual create invoice in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/PartnerManualCreateInvoice` | unwrapped | — | Not tested |
| Partner upload receipt in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/PartnerUploadReceipt` | unwrapped | — | Not tested |
| Payment approval callback in the charging service. | UNKNOWN | unknown | `/CreativeOne/Charging/PaymentApprovalCallback` | unwrapped | — | Not tested |

## Control (1)

| Action | Method | Classification | Endpoint | Input | Parameters | Live |
| --- | --- | --- | --- | --- | --- | --- |
| Creator risk check in the control service. | POST | action-or-mutation | `/CreativeOne/Control/CreatorRiskCheck` | data | `source`, `params` | Not tested |

## Creator (102)

| Action | Method | Classification | Endpoint | Input | Parameters | Live |
| --- | --- | --- | --- | --- | --- | --- |
| Admin get category threshold in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/AdminGetCategoryThreshold` | unwrapped | — | Not tested |
| Admin get register regions in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/AdminGetRegisterRegions` | unwrapped | — | Not tested |
| Admin operate category entity in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/AdminOperateCategoryEntity` | unwrapped | — | Not tested |
| Admin query category entity list in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/AdminQueryCategoryEntityList` | unwrapped | — | Not tested |
| Admin save category entity in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/AdminSaveCategoryEntity` | unwrapped | — | Not tested |
| Admin save category threshold in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/AdminSaveCategoryThreshold` | unwrapped | — | Not tested |
| Agency get creator binding link in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/AgencyGetCreatorBindingLink` | unwrapped | — | Not tested |
| Agency invite creator for binding in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/AgencyInviteCreatorForBinding` | unwrapped | — | Not tested |
| Batch read inhouse notice in the creator service. | POST | action-or-mutation | `/CreativeOne/Creator/BatchReadInhouseNotice` | data | `noticeIDList`, `readAll` | Not tested |
| Check creator media kit access in the creator service. | GET | read-only | `/CreativeOne/Creator/CheckCreatorMediaKitAccess` | none | — | Not tested |
| Check join source availability in the creator service. | GET | read-only | `/CreativeOne/Creator/CheckJoinSourceAvailability` | params | `channelCode` | Not tested |
| Check private pool link can be bound in the creator service. | GET | read-only | `/CreativeOne/Creator/CheckPrivatePoolLinkCanBeBound` | params | `channelCode` | Not tested |
| Client get creator price info in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/ClientGetCreatorPriceInfo` | unwrapped | — | Not tested |
| Create agency unbinding record in the creator service. | POST | action-or-mutation | `/CreativeOne/Creator/CreateAgencyUnbindingRecord` | data | `relationshipID` | Not tested |
| Create creator relationship in the creator service. | POST | action-or-mutation | `/CreativeOne/Creator/CreateCreatorRelationship` | data | `relationshipType`, `entityType`, `entityID`, `channelCode`, `privateCreatorNote`, `privateCreatorCategories` | Not tested |
| Creator exit activity in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/CreatorExitActivity` | unwrapped | — | Not tested |
| Creator get tto collabs profile in the creator service. | GET | read-only | `/CreativeOne/Creator/CreatorGetTTOCollabsProfile` | none | — | Not tested |
| Creator get tto collabs setting in the creator service. | GET | read-only | `/CreativeOne/Creator/CreatorGetTTOCollabsSetting` | none | — | Not tested |
| Creator join activity in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/CreatorJoinActivity` | unwrapped | — | Not tested |
| Creator query tto collabs item list in the creator service. | GET | read-only | `/CreativeOne/Creator/CreatorQueryTTOCollabsItemList` | params | `page`, `limit` | Not tested |
| Creator query tto collabs item play data in the creator service. | GET | read-only | `/CreativeOne/Creator/CreatorQueryTTOCollabsItemPlayData` | params | `page`, `limit` | Not tested |
| Creator register in the creator service. | POST | action-or-mutation | `/CreativeOne/Creator/CreatorRegister` | data | `protocolIDs`, `aioCode` | Not tested |
| Creator save tto collabs setting in the creator service. | POST | action-or-mutation | `/CreativeOne/Creator/CreatorSaveTTOCollabsSetting` | data | `setting` | Not tested |
| Delete creator media kit in the creator service. | POST | action-or-mutation | `/CreativeOne/Creator/DeleteCreatorMediaKit` | data | `mediaKitID` | Not tested |
| Download channel related creators in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/DownloadChannelRelatedCreators` | unwrapped | — | Not tested |
| Export private creator list in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/ExportPrivateCreatorList` | unwrapped | — | Not tested |
| Get agency cooperation records in the creator service. | GET | read-only | `/CreativeOne/Creator/GetAgencyCooperationRecords` | params | `unbindingRecordID` | Not tested |
| Get agency invite detail in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/GetAgencyInviteDetail` | unwrapped | — | Not tested |
| Get channel related creators in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/GetChannelRelatedCreators` | unwrapped | — | Not tested |
| Get creator activity info in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/GetCreatorActivityInfo` | unwrapped | — | Not tested |
| Get creator activity item list in the creator service. | GET | read-only | `/CreativeOne/Creator/GetCreatorActivityItemList` | params | `page`, `limit` | Not tested |
| Get creator appeal status in the creator service. | GET | read-only | `/CreativeOne/Creator/GetCreatorAppealStatus` | params | `appealType` | Not tested |
| Get creator banner config in the creator service. | GET | read-only | `/CreativeOne/Creator/GetCreatorBannerConfig` | params | `limit` | Not tested |
| Get creator base info in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/GetCreatorBaseInfo` | unwrapped | — | Not tested |
| Get creator benefit in the creator service. | GET | read-only | `/CreativeOne/Creator/GetCreatorBenefit` | params | `benefitDescIDList` | Not tested |
| Get creator historical contact in the creator service. | GET | read-only | `/CreativeOne/Creator/GetCreatorHistoricalContact` | none | — | Not tested |
| Get creator historical registration in the creator service. | GET | read-only | `/CreativeOne/Creator/GetCreatorHistoricalRegistration` | none | — | Not tested |
| Get creator incentive info in the creator service. | GET | read-only | `/CreativeOne/Creator/GetCreatorIncentiveInfo` | none | — | Not tested |
| Get creator media kit list in the creator service. | GET | read-only | `/CreativeOne/Creator/GetCreatorMediaKitList` | params | `page`, `limit` | Not tested |
| Get creator non sensitive profile in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/GetCreatorNonSensitiveProfile` | unwrapped | — | Not tested |
| Get creator oac premium price in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/GetCreatorOACPremiumPrice` | unwrapped | — | Not tested |
| Get creator order contact info in the creator service. | GET | read-only | `/CreativeOne/Creator/GetCreatorOrderContactInfo` | params | `contactID`, `infoType` | Not tested |
| Get creator order contact info by contact id in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/GetCreatorOrderContactInfoByContactID` | unwrapped | — | Not tested |
| Get creator portfolio list in the creator service. | GET | read-only | `/CreativeOne/Creator/GetCreatorPortfolioList` | params | `status`, `lang` | Not tested |
| Get creator profile in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/GetCreatorProfile` | unwrapped | — | Not tested |
| Get creator profile detail in the creator service. | GET | read-only | `/CreativeOne/Creator/GetCreatorProfileDetail` | none | — | Not tested |
| Get creator profile option list in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/GetCreatorProfileOptionList` | unwrapped | — | Not tested |
| Get creator profile progress in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/GetCreatorProfileProgress` | unwrapped | — | Not tested |
| Get creator register type in the creator service. | GET | read-only | `/CreativeOne/Creator/GetCreatorRegisterType` | params | `groupIDs`, `campaignID`, `creatorAgencyID`, `cooperationID`, `preAuthID`, `relationshipID`, `brandLinkID`, `aioCode` | Not tested |
| Get creator sensitive profile in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/GetCreatorSensitiveProfile` | unwrapped | — | Not tested |
| Get creator settings in the creator service. | GET | read-only | `/CreativeOne/Creator/GetCreatorSettings` | none | — | Not tested |
| Get creator shipping info in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/GetCreatorShippingInfo` | unwrapped | — | Not tested |
| Get creator stats data in the creator service. | GET | read-only | `/CreativeOne/Creator/GetCreatorStatsData` | none | — | Not tested |
| Get creator tt base info in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/GetCreatorTTBaseInfo` | unwrapped | — | Not tested |
| Get default media kit in the creator service. | GET | read-only | `/CreativeOne/Creator/GetDefaultMediaKit` | none | — | Not tested |
| Get feature switch in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/GetFeatureSwitch` | unwrapped | — | Not tested |
| Get inhouse notice list in the creator service. | GET | read-only | `/CreativeOne/Creator/GetInhouseNoticeList` | params | `page`, `limit` | Not tested |
| Get oac premium price config in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/GetOACPremiumPriceConfig` | unwrapped | — | Not tested |
| Get platform config in the creator service. | GET | read-only | `/CreativeOne/Creator/GetPlatformConfig` | none | — | Not tested |
| Get popup in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/GetPopup` | unwrapped | — | Not tested |
| Get portfolio video option list in the creator service. | GET | read-only | `/CreativeOne/Creator/GetPortfolioVideoOptionList` | params | `videoType`, `orderBy`, `page`, `limit`, `cursor` | Not tested |
| Get public video info in the creator service. | GET | read-only | `/CreativeOne/Creator/GetPublicVideoInfo` | params | `videoID` | Not tested |
| Get relationship detail in the creator service. | GET | read-only | `/CreativeOne/Creator/GetRelationshipDetail` | params | `relationshipID`, `aioClientID` | Not tested |
| M get creator oac premium price in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/MGetCreatorOACPremiumPrice` | unwrapped | — | Not tested |
| M get creator settings in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/MGetCreatorSettings` | unwrapped | — | Not tested |
| M get public video info in the creator service. | GET | read-only | `/CreativeOne/Creator/MGetPublicVideoInfo` | params | `videoIDList` | Not tested |
| Query creator handle info in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/QueryCreatorHandleInfo` | unwrapped | — | Not tested |
| Query creator relationship in the creator service. | GET | read-only | `/CreativeOne/Creator/QueryCreatorRelationship` | params | `relationshipType`, `packInfoType` | Not tested |
| Query private creator list in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/QueryPrivateCreatorList` | unwrapped | — | Not tested |
| Read can creator register in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/Read/CanCreatorRegister` | unwrapped | — | Not tested |
| Read get creator base info in the creator service. | GET | read-only | `/CreativeOne/Creator/Read/GetCreatorBaseInfo` | none | — | Not tested |
| Read preview get creator banner config list in the creator service. | GET | read-only | `/CreativeOne/Creator/Read/PreviewGetCreatorBannerConfigList` | params | `limit` | Not tested |
| Read preview get creator profile in the creator service. | GET | read-only | `/CreativeOne/Creator/Read/PreviewGetCreatorProfile` | none | — | Not tested |
| Read preview get creator rank latest slot in the creator service. | POST | action-or-mutation | `/CreativeOne/Creator/Read/PreviewGetCreatorRankLatestSlot` | none | — | Not tested |
| Read preview get creator stats data in the creator service. | GET | read-only | `/CreativeOne/Creator/Read/PreviewGetCreatorStatsData` | none | — | Not tested |
| Read preview get top contents list in the creator service. | GET | read-only | `/CreativeOne/Creator/Read/PreviewGetTopContentsList` | params | `periodDimension`, `periodEndTimestamp`, `orderByMetric`, `countryCode`, `contentLabelIDs`, `organicOnly`, `limit`, `page` | Not tested |
| Read preview get top contents overview in the creator service. | GET | read-only | `/CreativeOne/Creator/Read/PreviewGetTopContentsOverview` | none | — | Not tested |
| Read preview m get creator rank list in the creator service. | POST | action-or-mutation | `/CreativeOne/Creator/Read/PreviewMGetCreatorRankList` | data | `itemList` | Not tested |
| Read preview m get public video info in the creator service. | GET | read-only | `/CreativeOne/Creator/Read/PreviewMGetPublicVideoInfo` | params | `videoIDList` | Not tested |
| Read preview save creator feedback in the creator service. | GET | read-only | `/CreativeOne/Creator/Read/PreviewSaveCreatorFeedback` | params | `feedbackType`, `score`, `content`, `entityID`, `entityType` | Not tested |
| Read popup in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/ReadPopup` | unwrapped | — | Not tested |
| Respond agency invite in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/RespondAgencyInvite` | unwrapped | — | Not tested |
| Save creator allowlist in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/SaveCreatorAllowlist` | unwrapped | — | Not tested |
| Save creator appeal in the creator service. | POST | action-or-mutation | `/CreativeOne/Creator/SaveCreatorAppeal` | data | `appealType`, `appealDataList` | Not tested |
| Save creator feedback in the creator service. | GET | read-only | `/CreativeOne/Creator/SaveCreatorFeedback` | params | `feedbackType`, `score`, `content`, `entityID`, `entityType` | Not tested |
| Save creator media kit in the creator service. | POST | action-or-mutation | `/CreativeOne/Creator/SaveCreatorMediaKit` | data | `mediaKitInfo` | Not tested |
| Update agency unbinding record in the creator service. | POST | action-or-mutation | `/CreativeOne/Creator/UpdateAgencyUnbindingRecord` | data | `unbindingRecordID`, `operation` | Not tested |
| Update creator category in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/UpdateCreatorCategory` | unwrapped | — | Not tested |
| Update creator non sensitive profile in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/UpdateCreatorNonSensitiveProfile` | unwrapped | — | Not tested |
| Update creator order contact info in the creator service. | POST | action-or-mutation | `/CreativeOne/Creator/UpdateCreatorOrderContactInfo` | data | `infoType`, `infoDetail`, `contactID` | Not tested |
| Update creator portfolio list in the creator service. | POST | action-or-mutation | `/CreativeOne/Creator/UpdateCreatorPortfolioList` | data | `videoList`, `actionType` | Not tested |
| Update creator profile in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/UpdateCreatorProfile` | unwrapped | — | Not tested |
| Update creator profile detail in the creator service. | POST | action-or-mutation | `/CreativeOne/Creator/UpdateCreatorProfileDetail` | data | `profileTypeList`, `creatorProfile`, `isMigrate` | Not tested |
| Update creator relationship in the creator service. | POST | action-or-mutation | `/CreativeOne/Creator/UpdateCreatorRelationship` | data | `relationshipID`, `agree` | Not tested |
| Update creator sensitive profile in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/UpdateCreatorSensitiveProfile` | unwrapped | — | Not tested |
| Update creator settings in the creator service. | POST | action-or-mutation | `/CreativeOne/Creator/UpdateCreatorSettings` | data | `settingsTypeList`, `creatorSettings` | Not tested |
| Update creator shipping info in the creator service. | POST | action-or-mutation | `/CreativeOne/Creator/UpdateCreatorShippingInfo` | data | `creatorShippingInfo`, `shippingContactID` | Not tested |
| User check tto collabs verify code in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/UserCheckTTOCollabsVerifyCode` | unwrapped | — | Not tested |
| User gen tto collabs saved list url in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/UserGenTTOCollabsSavedListURL` | unwrapped | — | Not tested |
| User get tto collabs saved creator list in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/UserGetTTOCollabsSavedCreatorList` | unwrapped | — | Not tested |
| User operate tto collabs creator in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/UserOperateTTOCollabsCreator` | unwrapped | — | Not tested |
| User send tto collabs verify code in the creator service. | UNKNOWN | unknown | `/CreativeOne/Creator/UserSendTTOCollabsVerifyCode` | unwrapped | — | Not tested |

## DataSpace (45)

| Action | Method | Classification | Endpoint | Input | Parameters | Live |
| --- | --- | --- | --- | --- | --- | --- |
| Appeal admin get appeal record list in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/Appeal/AdminGetAppealRecordList` | unwrapped | — | Not tested |
| Appeal admin operate appeal in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/Appeal/AdminOperateAppeal` | unwrapped | — | Not tested |
| Brand library admin create or modify brand info in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/AdminCreateOrModifyBrandInfo` | unwrapped | — | Not tested |
| Brand library admin get brand exclusive label in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/AdminGetBrandExclusiveLabel` | unwrapped | — | Not tested |
| Brand library admin get brand list in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/AdminGetBrandList` | unwrapped | — | Not tested |
| Brand library admin get brand related accounts in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/AdminGetBrandRelatedAccounts` | unwrapped | — | Not tested |
| Brand library admin get client brand list in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/AdminGetClientBrandList` | unwrapped | — | Not tested |
| Brand library admin get ttu id by name in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/AdminGetTTUIDByName` | unwrapped | — | Not tested |
| Brand library admin operate brand in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/AdminOperateBrand` | unwrapped | — | Not tested |
| Brand library admin update brand related accounts in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/AdminUpdateBrandRelatedAccounts` | unwrapped | — | Not tested |
| Brand library brand verify in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/BrandVerify` | unwrapped | — | Not tested |
| Brand library bypass demote undisclosed item policy in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/BypassDemoteUndisclosedItemPolicy` | unwrapped | — | Not tested |
| Brand library client appeal brand verify in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/ClientAppealBrandVerify` | unwrapped | — | Not tested |
| Brand library client create or modify brand in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/ClientCreateOrModifyBrand` | unwrapped | — | Not tested |
| Brand library client get brand by page in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/ClientGetBrandByPage` | unwrapped | — | Not tested |
| Brand library client get brand info in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/ClientGetBrandInfo` | unwrapped | — | Not tested |
| Brand library client get brand list in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/ClientGetBrandList` | unwrapped | — | Not tested |
| Brand library client get ttu id by name in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/ClientGetTTUIDByName` | unwrapped | — | Not tested |
| Brand library creator appeal for undisclosed item in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/CreatorAppealForUndisclosedItem` | unwrapped | — | Not tested |
| Brand library creator get algo recommend brand in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/CreatorGetAlgoRecommendBrand` | unwrapped | — | Not tested |
| Brand library creator get recommend brand list in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/CreatorGetRecommendBrandList` | unwrapped | — | Not tested |
| Brand library creator get undisclosed flagged item infos in the data space service. | POST | action-or-mutation | `/CreativeOne/DataSpace/BrandLibrary/CreatorGetUndisclosedFlaggedItemInfos` | data | `page`, `limit` | Not tested |
| Brand library creator get undisclosed item info in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/CreatorGetUndisclosedItemInfo` | unwrapped | — | Not tested |
| Brand library creator get undisclosed managed item infos in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/CreatorGetUndisclosedManagedItemInfos` | unwrapped | — | Not tested |
| Brand library creator response recommend brand in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/CreatorResponseRecommendBrand` | unwrapped | — | Not tested |
| Brand library get manual review appeals in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/GetManualReviewAppeals` | unwrapped | — | Not tested |
| Brand library get share link user info in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/GetShareLinkUserInfo` | unwrapped | — | Not tested |
| Brand library operate undisclosed item appeal request in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/OperateUndisclosedItemAppealRequest` | unwrapped | — | Not tested |
| Brand library update content suite auto sync in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/UpdateContentSuiteAutoSync` | unwrapped | — | Not tested |
| Brand library update content suite share link in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/BrandLibrary/UpdateContentSuiteShareLink` | unwrapped | — | Not tested |
| Job delete es mapping in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/Job/DeleteESMapping` | unwrapped | — | Not tested |
| Job delete field mapping in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/Job/DeleteFieldMapping` | unwrapped | — | Not tested |
| Job get field mapping in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/Job/GetFieldMapping` | unwrapped | — | Not tested |
| Job get jobs in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/Job/GetJobs` | unwrapped | — | Not tested |
| Job get scheduling record in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/Job/GetSchedulingRecord` | unwrapped | — | Not tested |
| Job save field mapping in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/Job/SaveFieldMapping` | unwrapped | — | Not tested |
| Job save jobs in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/Job/SaveJobs` | unwrapped | — | Not tested |
| Job update status in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/Job/UpdateStatus` | unwrapped | — | Not tested |
| Meta data delete fields in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/MetaData/DeleteFields` | unwrapped | — | Not tested |
| Meta data get fields in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/MetaData/GetFields` | unwrapped | — | Not tested |
| Meta data get schemas in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/MetaData/GetSchemas` | unwrapped | — | Not tested |
| Meta data get sources in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/MetaData/GetSources` | unwrapped | — | Not tested |
| Meta data save fields in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/MetaData/SaveFields` | unwrapped | — | Not tested |
| Meta data save schemas in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/MetaData/SaveSchemas` | unwrapped | — | Not tested |
| Meta data save sources in the data space service. | UNKNOWN | unknown | `/CreativeOne/DataSpace/MetaData/SaveSources` | unwrapped | — | Not tested |

## MatchLabel (1)

| Action | Method | Classification | Endpoint | Input | Parameters | Live |
| --- | --- | --- | --- | --- | --- | --- |
| Get match label tree by type in the match label service. | GET | read-only | `/CreativeOne/MatchLabel/GetMatchLabelTreeByType` | params | `labelType`, `labelLevel`, `labelStatus`, `simpleTree`, `labelVersion` | Not tested |

## MatchMaking (47)

| Action | Method | Classification | Endpoint | Input | Parameters | Live |
| --- | --- | --- | --- | --- | --- | --- |
| Admin creator search in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/AdminCreatorSearch` | unwrapped | — | Not tested |
| Admin export search result to lark sheet in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/AdminExportSearchResultToLarkSheet` | unwrapped | — | Not tested |
| Admin get search result creator in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/AdminGetSearchResultCreator` | unwrapped | — | Not tested |
| Admin get search results in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/AdminGetSearchResults` | unwrapped | — | Not tested |
| Admin operate search result creators in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/AdminOperateSearchResultCreators` | unwrapped | — | Not tested |
| Agency query creator by handle name in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/AgencyQueryCreatorByHandleName` | unwrapped | — | Not tested |
| Agent asset impressions in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/AgentAssetImpressions` | unwrapped | — | Not tested |
| Client m get creator rank list in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/ClientMGetCreatorRankList` | unwrapped | — | Not tested |
| Client query creator in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/ClientQueryCreator` | unwrapped | — | Not tested |
| Creator get campaign list in the match making service. | POST | action-or-mutation | `/CreativeOne/MatchMaking/CreatorGetCampaignList` | data | `page`, `limit`, `reqTrackID`, `filter`, `sortType`, `scene`, `abParams` | Not tested |
| Creator get rank latest slot in the match making service. | POST | action-or-mutation | `/CreativeOne/MatchMaking/CreatorGetRankLatestSlot` | data | `needLoaderList`, `needLatestData`, `params` | Not tested |
| Creator get search list in the match making service. | POST | action-or-mutation | `/CreativeOne/MatchMaking/CreatorGetSearchList` | data | `page`, `limit`, `keyword`, `searchScene`, `searchType`, `abParams`, `chargingStatus` | Not tested |
| Creator get search suggest in the match making service. | POST | action-or-mutation | `/CreativeOne/MatchMaking/CreatorGetSearchSuggest` | data | `keyword`, `abParams`, `searchScene`, `limit` | Not tested |
| Creator m get creator rank list in the match making service. | POST | action-or-mutation | `/CreativeOne/MatchMaking/CreatorMGetCreatorRankList` | data | `itemList` | Not tested |
| Diagnose campaign feed visibility in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/DiagnoseCampaignFeedVisibility` | unwrapped | — | Not tested |
| Download creator list from ttms in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/DownloadCreatorListFromTTMS` | unwrapped | — | Not tested |
| Export creator list from ttms in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/ExportCreatorListFromTTMS` | unwrapped | — | Not tested |
| Get agency match creator list in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/GetAgencyMatchCreatorList` | unwrapped | — | Not tested |
| Get client intention in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/GetClientIntention` | unwrapped | — | Not tested |
| Get creator rank latest slot in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/GetCreatorRankLatestSlot` | unwrapped | — | Not tested |
| Get creator rank list config in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/GetCreatorRankListConfig` | unwrapped | — | Not tested |
| Get data vdc region by country in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/GetDataVDCRegionByCountry` | unwrapped | — | Not tested |
| Get inspiration list in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/GetInspirationList` | unwrapped | — | Not tested |
| Get inspiration pills in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/GetInspirationPills` | unwrapped | — | Not tested |
| Get inspiration template filter in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/GetInspirationTemplateFilter` | unwrapped | — | Not tested |
| Get pop up selling point list in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/GetPopUpSellingPointList` | unwrapped | — | Not tested |
| Get query word is person name in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/GetQueryWordIsPersonName` | unwrapped | — | Not tested |
| Get rank list category by type in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/GetRankListCategoryByType` | unwrapped | — | Not tested |
| Inner query search filter option in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/InnerQuerySearchFilterOption` | unwrapped | — | Not tested |
| M get ranking list by id in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/MGetRankingListByID` | unwrapped | — | Not tested |
| Pre generate aio creator account in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/PreGenerateAioCreatorAccount` | unwrapped | — | Not tested |
| Query aio creator id by name in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/QueryAIOCreatorIDByName` | unwrapped | — | Not tested |
| Query campaign recommended creators in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/QueryCampaignRecommendedCreators` | unwrapped | — | Not tested |
| Query creator list by page in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/QueryCreatorListByPage` | unwrapped | — | Not tested |
| Query creator list from ttms in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/QueryCreatorListFromTTMS` | unwrapped | — | Not tested |
| Query creator rank list in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/QueryCreatorRankList` | unwrapped | — | Not tested |
| Query creator rank list for seo in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/QueryCreatorRankListForSeo` | unwrapped | — | Not tested |
| Query creator square in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/QueryCreatorSquare` | unwrapped | — | Not tested |
| Query partner creator square in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/QueryPartnerCreatorSquare` | unwrapped | — | Not tested |
| Query partner search filter option in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/QueryPartnerSearchFilterOption` | unwrapped | — | Not tested |
| Query partner search suggest words in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/QueryPartnerSearchSuggestWords` | unwrapped | — | Not tested |
| Query search filter option in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/QuerySearchFilterOption` | unwrapped | — | Not tested |
| Query search suggest words in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/QuerySearchSuggestWords` | unwrapped | — | Not tested |
| Query similar creators in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/QuerySimilarCreators` | unwrapped | — | Not tested |
| Query un verified creator square in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/QueryUnVerifiedCreatorSquare` | unwrapped | — | Not tested |
| Search creator by llm in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/SearchCreatorByLLM` | unwrapped | — | Not tested |
| Search tiktok user in the match making service. | UNKNOWN | unknown | `/CreativeOne/MatchMaking/SearchTikTokUser` | unwrapped | — | Not tested |

## MatchPack (6)

| Action | Method | Classification | Endpoint | Input | Parameters | Live |
| --- | --- | --- | --- | --- | --- | --- |
| Get tt creator card in the match pack service. | POST | action-or-mutation | `/CreativeOne/MatchPack/GetTTCreatorCard` | data | `needLoaderList`, `needLatestData`, `params` | Not tested |
| M get creators card in the match pack service. | UNKNOWN | unknown | `/CreativeOne/MatchPack/MGetCreatorsCard` | unwrapped | — | Not tested |
| M get creators card by admin in the match pack service. | UNKNOWN | unknown | `/CreativeOne/MatchPack/MGetCreatorsCardByAdmin` | unwrapped | — | Not tested |
| M get creators card by local in the match pack service. | UNKNOWN | unknown | `/CreativeOne/MatchPack/MGetCreatorsCardByLocal` | unwrapped | — | Not tested |
| M get creators card for seo in the match pack service. | UNKNOWN | unknown | `/CreativeOne/MatchPack/MGetCreatorsCardForSeo` | unwrapped | — | Not tested |
| M get items insights in the match pack service. | UNKNOWN | unknown | `/CreativeOne/MatchPack/MGetItemsInsights` | unwrapped | — | Not tested |

## OrderCommand (22)

| Action | Method | Classification | Endpoint | Input | Parameters | Live |
| --- | --- | --- | --- | --- | --- | --- |
| Creator accept opportunity in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorAcceptOpportunity` | data | `opportunityID`, `screeningAnswers`, `contactID`, `contactInfoOppoShown`, `shippingInfoID`, `negotiatePrice100K`, `proposalMessage`, `skuProductID`, `isVideoAuthorizationToggleOn` | Not tested |
| Creator answer check in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorAnswerCheck` | data | `campaignID`, `screeningAnswers`, `opportunityID`, `partnerCampaignID` | Not tested |
| Creator apply campaign in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorApplyCampaign` | data | `campaignID`, `screeningAnswers`, `contactID`, `contactInfoOppoShown`, `shippingInfoID`, `negotiatePrice100K`, `proposalMessage`, `flatFee100K`, `currency`, `skuProductID`, `isVideoAuthorizationToggleOn`, `partnerCampaignID` | Not tested |
| Creator apply multi products in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorApplyMultiProducts` | data | `campaignID`, `screeningAnswers`, `contactID`, `contactInfoOppoShown`, `shippingInfoID`, `skuProductIDs`, `flatFee100K`, `currency`, `isVideoAuthorizationToggleOn` | Not tested |
| Creator cancel order in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorCancelOrder` | data | `orderID`, `cancellationReasons` | Not tested |
| Creator create negotiation in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorCreateNegotiation` | data | `opportunityID`, `negotiatePrice100K`, `proposalMessage` | Not tested |
| Creator extend submission date in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorExtendSubmissionDate` | data | `orderID`, `reason` | Not tested |
| Creator handle sparkads in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorHandleSparkAds` | data | `orderID`, `itemID`, `action` | Not tested |
| Creator join campaign v2 in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorJoinCampaignV2` | data | `campaignID`, `joinSource`, `flatFee100K`, `currency`, `isVideoAuthorizationToggleOn`, `partnerCampaignID` | Not tested |
| Creator join wait list in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorJoinWaitList` | data | `campaignID`, `flatFee100K`, `currency`, `isVideoAuthorizationToggleOn` | Not tested |
| Creator operate content cooperation in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorOperateContentCooperation` | data | `cooperationID`, `operation`, `authDays`, `otherRejectReason`, `rejectReason`, `promotionLink` | Not tested |
| Creator pre authorize content cooperation in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorPreAuthorizeContentCooperation` | data | `authDays`, `operation`, `optoutReason`, `reasonDetail` | Not tested |
| Creator quit opportunity in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorQuitOpportunity` | data | `opportunityID`, `cancellationReasons` | Not tested |
| Creator quit wait list in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorQuitWaitList` | data | `opportunityID` | Not tested |
| Creator receive product in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorReceiveProduct` | data | `orderID` | Not tested |
| Creator reject campaign link item in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorRejectCampaignLinkItem` | data | `orderID` | Not tested |
| Creator reject opportunity in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorRejectOpportunity` | data | `opportunityID`, `reasons` | Not tested |
| Creator reply historical ba sparkads auth in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorReplyHistoricalBASparkAdsAuth` | data | `authStatus` | Not tested |
| Creator reply video authorization in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorReplyVideoAuthorization` | data | `orderID`, `isAccept`, `creatorAuthorizationToggleConfig` | Not tested |
| Creator submit video appeal in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorSubmitVideoAppeal` | data | `orderID`, `videoID`, `contentType`, `reasonList`, `appealType` | Not tested |
| Creator upload creative in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorUploadCreative` | data | `videoID`, `videoName`, `orderID`, `videoMeta` | Not tested |
| Creator withdraw creative in the order command service. | POST | action-or-mutation | `/CreativeOne/OrderCommand/CreatorWithdrawCreative` | data | `orderID` | Not tested |

## OrderQuery (218)

| Action | Method | Classification | Endpoint | Input | Parameters | Live |
| --- | --- | --- | --- | --- | --- | --- |
| Admin check support one click video submission in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminCheckSupportOneClickVideoSubmission` | unwrapped | — | Not tested |
| Admin creator collab list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminCreatorCollabList` | unwrapped | — | Not tested |
| Admin currency conversion in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminCurrencyConversion` | unwrapped | — | Not tested |
| Admin get agency match making invitations in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminGetAgencyMatchMakingInvitations` | unwrapped | — | Not tested |
| Admin get auto brief asset video audit status in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminGetAutoBriefAssetVideoAuditStatus` | unwrapped | — | Not tested |
| Admin get auto brief detail in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminGetAutoBriefDetail` | unwrapped | — | Not tested |
| Admin get auto brief video generation input in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminGetAutoBriefVideoGenerationInput` | unwrapped | — | Not tested |
| Admin get brand event in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminGetBrandEvent` | unwrapped | — | Not tested |
| Admin get brand event list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminGetBrandEventList` | unwrapped | — | Not tested |
| Admin get brand package in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminGetBrandPackage` | unwrapped | — | Not tested |
| Admin get brand project list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminGetBrandProjectList` | unwrapped | — | Not tested |
| Admin get buzz campaign quota detail in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminGetBuzzCampaignQuotaDetail` | unwrapped | — | Not tested |
| Admin get campaign detail in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminGetCampaignDetail` | unwrapped | — | Not tested |
| Admin get campaign order list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminGetCampaignOrderList` | unwrapped | — | Not tested |
| Admin get creator spot in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminGetCreatorSpot` | unwrapped | — | Not tested |
| Admin get creator video list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminGetCreatorVideoList` | unwrapped | — | Not tested |
| Admin get file list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminGetFileList` | unwrapped | — | Not tested |
| Admin get folder list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminGetFolderList` | unwrapped | — | Not tested |
| Admin get mission payment list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminGetMissionPaymentList` | unwrapped | — | Not tested |
| Admin get partner campaign custom notes in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminGetPartnerCampaignCustomNotes` | unwrapped | — | Not tested |
| Admin granted spot list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminGrantedSpotList` | unwrapped | — | Not tested |
| Admin list agency grant spot batch in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminListAgencyGrantSpotBatch` | unwrapped | — | Not tested |
| Admin list agency price config category in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminListAgencyPriceConfigCategory` | unwrapped | — | Not tested |
| Admin list country cpm level in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminListCountryCPMLevel` | unwrapped | — | Not tested |
| Admin list country packages in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminListCountryPackages` | unwrapped | — | Not tested |
| Admin list country price configs in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminListCountryPriceConfigs` | unwrapped | — | Not tested |
| Admin list partner matchmaking rules in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminListPartnerMatchmakingRules` | unwrapped | — | Not tested |
| Admin query auto brief list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminQueryAutoBriefList` | unwrapped | — | Not tested |
| Admin query buzz auto match making config in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminQueryBuzzAutoMatchMakingConfig` | unwrapped | — | Not tested |
| Admin query buzz country config in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminQueryBuzzCountryConfig` | unwrapped | — | Not tested |
| Admin query global business region list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminQueryGlobalBusinessRegionList` | unwrapped | — | Not tested |
| Admin query global pj list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AdminQueryGlobalPJList` | unwrapped | — | Not tested |
| Agency collaboration list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AgencyCollaborationList` | unwrapped | — | Not tested |
| Agency collaboration status list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AgencyCollaborationStatusList` | unwrapped | — | Not tested |
| Agency get campaign detail in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AgencyGetCampaignDetail` | unwrapped | — | Not tested |
| Agency get client contact info with token in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AgencyGetClientContactInfoWithToken` | unwrapped | — | Not tested |
| Agency get collab detail with token in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AgencyGetCollabDetailWithToken` | unwrapped | — | Not tested |
| Agency get collaboration list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AgencyGetCollaborationList` | unwrapped | — | Not tested |
| Agency get creator video list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AgencyGetCreatorVideoList` | unwrapped | — | Not tested |
| Agency get invited creators in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AgencyGetInvitedCreators` | unwrapped | — | Not tested |
| Agency get match making cnt in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AgencyGetMatchMakingCnt` | unwrapped | — | Not tested |
| Agency get match making cooperations in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AgencyGetMatchMakingCooperations` | unwrapped | — | Not tested |
| Agency get match making invitations in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AgencyGetMatchMakingInvitations` | unwrapped | — | Not tested |
| Agency get match making negotiation history in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AgencyGetMatchMakingNegotiationHistory` | unwrapped | — | Not tested |
| Agency get mission video list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AgencyGetMissionVideoList` | unwrapped | — | Not tested |
| Agency get order detail in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AgencyGetOrderDetail` | unwrapped | — | Not tested |
| Agency get partner campaign match data in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AgencyGetPartnerCampaignMatchData` | unwrapped | — | Not tested |
| Agency get partner campaign order count in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AgencyGetPartnerCampaignOrderCount` | unwrapped | — | Not tested |
| Agency get partner campaign order list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/AgencyGetPartnerCampaignOrderList` | unwrapped | — | Not tested |
| Clp client recommend partner in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CLPClientRecommendPartner` | unwrapped | — | Not tested |
| Campaign discovery for partner in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CampaignDiscoveryForPartner` | unwrapped | — | Not tested |
| Campaign list for admin in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CampaignListForAdmin` | unwrapped | — | Not tested |
| Campaign oac status in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CampaignOacStatus` | unwrapped | — | Not tested |
| Campaign opportunity count in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CampaignOpportunityCount` | unwrapped | — | Not tested |
| Campaign order count in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CampaignOrderCount` | unwrapped | — | Not tested |
| Campaign video count in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CampaignVideoCount` | unwrapped | — | Not tested |
| Check delegate campaign has opportunity in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CheckDelegateCampaignHasOpportunity` | unwrapped | — | Not tested |
| Check partner confirm shipment available in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CheckPartnerConfirmShipmentAvailable` | unwrapped | — | Not tested |
| Check ttam payment module allow list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CheckTTAMPaymentModuleAllowList` | unwrapped | — | Not tested |
| Client batch check wish creators in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientBatchCheckWishCreators` | unwrapped | — | Not tested |
| Client batch get item preview in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientBatchGetItemPreview` | unwrapped | — | Not tested |
| Client campaign count in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientCampaignCount` | unwrapped | — | Not tested |
| Client campaign detail in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientCampaignDetail` | unwrapped | — | Not tested |
| Client campaign overview in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientCampaignOverview` | unwrapped | — | Not tested |
| Client campaign spent budget timeline in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientCampaignSpentBudgetTimeline` | unwrapped | — | Not tested |
| Client check creators campaign qualification in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientCheckCreatorsCampaignQualification` | unwrapped | — | Not tested |
| Client collaboration list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientCollaborationList` | unwrapped | — | Not tested |
| Client collaboration list v2 in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientCollaborationListV2` | unwrapped | — | Not tested |
| Client collaboration order list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientCollaborationOrderList` | unwrapped | — | Not tested |
| Client collaboration video list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientCollaborationVideoList` | unwrapped | — | Not tested |
| Client collaboration video list v2 in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientCollaborationVideoListV2` | unwrapped | — | Not tested |
| Client collaboration video list v3 in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientCollaborationVideoListV3` | unwrapped | — | Not tested |
| Client download content cooperations in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientDownloadContentCooperations` | unwrapped | — | Not tested |
| Client draft campaign list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientDraftCampaignList` | unwrapped | — | Not tested |
| Client export content cooperations in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientExportContentCooperations` | unwrapped | — | Not tested |
| Client get brand event in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetBrandEvent` | unwrapped | — | Not tested |
| Client get brand event list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetBrandEventList` | unwrapped | — | Not tested |
| Client get brand project detail in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetBrandProjectDetail` | unwrapped | — | Not tested |
| Client get brand project list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetBrandProjectList` | unwrapped | — | Not tested |
| Client get campaign auto brief in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetCampaignAutoBrief` | unwrapped | — | Not tested |
| Client get campaign count for data centers in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetCampaignCountForDataCenters` | unwrapped | — | Not tested |
| Client get campaign invite draft list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetCampaignInviteDraftList` | unwrapped | — | Not tested |
| Client get campaign list for mmm in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetCampaignListForMMM` | unwrapped | — | Not tested |
| Client get campaign seat by campaign ids in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetCampaignSeatByCampaignIDs` | unwrapped | — | Not tested |
| Client get collab cnt in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetCollabCnt` | unwrapped | — | Not tested |
| Client get collaboration stage count in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetCollaborationStageCount` | unwrapped | — | Not tested |
| Client get content cooperation detail in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetContentCooperationDetail` | unwrapped | — | Not tested |
| Client get content cooperation quota in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetContentCooperationQuota` | unwrapped | — | Not tested |
| Client get content cooperations in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetContentCooperations` | unwrapped | — | Not tested |
| Client get creator orders in campaign in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetCreatorOrdersInCampaign` | unwrapped | — | Not tested |
| Client get dark launch config in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetDarkLaunchConfig` | unwrapped | — | Not tested |
| Client get empty brief template in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetEmptyBriefTemplate` | unwrapped | — | Not tested |
| Client get file list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetFileList` | unwrapped | — | Not tested |
| Client get folder list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetFolderList` | unwrapped | — | Not tested |
| Client get has y in feed before in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetHasYInFeedBefore` | unwrapped | — | Not tested |
| Client get if partner support online in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetIfPartnerSupportOnline` | unwrapped | — | Not tested |
| Client get mission order video list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetMissionOrderVideoList` | unwrapped | — | Not tested |
| Client get one more info in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetOneMoreInfo` | unwrapped | — | Not tested |
| Client get opportunity detail in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetOpportunityDetail` | unwrapped | — | Not tested |
| Client get order detail in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetOrderDetail` | unwrapped | — | Not tested |
| Client get order tracking info in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetOrderTrackingInfo` | unwrapped | — | Not tested |
| Client get pe campaign video cnt in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetPECampaignVideoCnt` | unwrapped | — | Not tested |
| Client get partner campaign refund in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetPartnerCampaignRefund` | unwrapped | — | Not tested |
| Client get partner delegate video list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetPartnerDelegateVideoList` | unwrapped | — | Not tested |
| Client get product list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetProductList` | unwrapped | — | Not tested |
| Client get share history in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetShareHistory` | unwrapped | — | Not tested |
| Client get video rejection quota in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGetVideoRejectionQuota` | unwrapped | — | Not tested |
| Client global campaign count by country in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGlobalCampaignCountByCountry` | unwrapped | — | Not tested |
| Client global campaign list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientGlobalCampaignList` | unwrapped | — | Not tested |
| Client m get brand link detail in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientMGetBrandLinkDetail` | unwrapped | — | Not tested |
| Client pending collaboration list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientPendingCollaborationList` | unwrapped | — | Not tested |
| Client physical product list v2 in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientPhysicalProductListV2` | unwrapped | — | Not tested |
| Client publish campaign list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientPublishCampaignList` | unwrapped | — | Not tested |
| Client query drama order video list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientQueryDramaOrderVideoList` | unwrapped | — | Not tested |
| Client query partner exchange campaign concept in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientQueryPartnerExchangeCampaignConcept` | unwrapped | — | Not tested |
| Client query partner exchange campaign creative in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientQueryPartnerExchangeCampaignCreative` | unwrapped | — | Not tested |
| Client query partner exchange campaign item in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientQueryPartnerExchangeCampaignItem` | unwrapped | — | Not tested |
| Client query ttcc campaign detail in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientQueryTTCCCampaignDetail` | unwrapped | — | Not tested |
| Client query ttcc campaign list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientQueryTTCCCampaignList` | unwrapped | — | Not tested |
| Client search product infos in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientSearchProductInfos` | unwrapped | — | Not tested |
| Client select creator campaign list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientSelectCreatorCampaignList` | unwrapped | — | Not tested |
| Client select partner campaign list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientSelectPartnerCampaignList` | unwrapped | — | Not tested |
| Client todo list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/ClientTodoList` | unwrapped | — | Not tested |
| Creator analytic order info in the order query service. | GET | read-only | `/CreativeOne/OrderQuery/CreatorAnalyticOrderInfo` | params | `itemID`, `videoID` | Not tested |
| Creator campaign management homepage in the order query service. | GET | read-only | `/CreativeOne/OrderQuery/CreatorCampaignManagementHomepage` | none | — | Validated 2026-09-03 |
| Creator collab list in the order query service. | GET | read-only | `/CreativeOne/OrderQuery/CreatorCollabList` | params | `collabStage`, `limit`, `page`, `campaignID` | Validated 2026-09-03 |
| Creator get blast details in the order query service. | GET | read-only | `/CreativeOne/OrderQuery/CreatorGetBlastDetails` | params | `blastID` | Not tested |
| Creator get brand history video in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CreatorGetBrandHistoryVideo` | unwrapped | — | Not tested |
| Creator get brand history video count in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CreatorGetBrandHistoryVideoCount` | unwrapped | — | Not tested |
| Creator get brand link detail in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CreatorGetBrandLinkDetail` | unwrapped | — | Not tested |
| Creator get campaign remaining seat by campaign ids in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CreatorGetCampaignRemainingSeatByCampaignIDs` | unwrapped | — | Not tested |
| Creator get collab detail in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CreatorGetCollabDetail` | unwrapped | — | Not tested |
| Creator get collab detail for unlogin in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CreatorGetCollabDetailForUnlogin` | unwrapped | — | Not tested |
| Creator get collab detail v2 in the order query service. | GET | read-only | `/CreativeOne/OrderQuery/CreatorGetCollabDetailV2` | params | `campaignID`, `opportunityID`, `orderID`, `creatorAgencyID`, `joinSource`, `partnerCampaignID` | Validated 2026-09-03 |
| Creator get commerce hashtag in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CreatorGetCommerceHashtag` | unwrapped | — | Not tested |
| Creator get content cooperation detail in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CreatorGetContentCooperationDetail` | unwrapped | — | Not tested |
| Creator get content cooperation detail by aioid in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CreatorGetContentCooperationDetailByAioid` | unwrapped | — | Not tested |
| Creator get content cooperation detail by ttuid in the order query service. | GET | read-only | `/CreativeOne/OrderQuery/CreatorGetContentCooperationDetailByTtuid` | params | `cooperationID` | Not tested |
| Creator get file list in the order query service. | GET | read-only | `/CreativeOne/OrderQuery/CreatorGetFileList` | params | `campaignID`, `folderID`, `orderType`, `limit`, `page` | Validated 2026-09-03 |
| Creator get folder list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CreatorGetFolderList` | unwrapped | — | Not tested |
| Creator get folder tree in the order query service. | GET | read-only | `/CreativeOne/OrderQuery/CreatorGetFolderTree` | params | `campaignID` | Validated 2026-09-03 |
| Creator get generated content in the order query service. | GET | read-only | `/CreativeOne/OrderQuery/CreatorGetGeneratedContent` | params | `campaignID`, `generateAction`, `taskID` | Not tested |
| Creator get hashtag detail in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CreatorGetHashtagDetail` | unwrapped | — | Not tested |
| Creator get historical ba sparkads auth status in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CreatorGetHistoricalBASparkAdsAuthStatus` | unwrapped | — | Not tested |
| Creator get linking request by campaign id in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CreatorGetLinkingRequestByCampaignID` | unwrapped | — | Not tested |
| Creator get linking request by id in the order query service. | GET | read-only | `/CreativeOne/OrderQuery/CreatorGetLinkingRequestByID` | params | `linkingRequestID` | Not tested |
| Creator get mission submissions in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CreatorGetMissionSubmissions` | unwrapped | — | Not tested |
| Creator get mission top video list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CreatorGetMissionTopVideoList` | unwrapped | — | Not tested |
| Creator get order detail in the order query service. | GET | read-only | `/CreativeOne/OrderQuery/CreatorGetOrderDetail` | params | `orderID` | Validated 2026-09-03 |
| Creator get order detail for unlogin in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CreatorGetOrderDetailForUnlogin` | unwrapped | — | Not tested |
| Creator get order tracking info in the order query service. | GET | read-only | `/CreativeOne/OrderQuery/CreatorGetOrderTrackingInfo` | params | `orderID` | Validated 2026-09-03 |
| Creator get post item list in the order query service. | GET | read-only | `/CreativeOne/OrderQuery/CreatorGetPostItemList` | params | `page`, `limit`, `scene`, `orderID`, `brandLinkID` | Validated 2026-09-03 |
| Creator get pre authorization status in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CreatorGetPreAuthorizationStatus` | unwrapped | — | Not tested |
| Creator get pre authorization status by aioid in the order query service. | GET | read-only | `/CreativeOne/OrderQuery/CreatorGetPreAuthorizationStatusByAioid` | none | — | Not tested |
| Creator get pre authorization status by ttuid in the order query service. | GET | read-only | `/CreativeOne/OrderQuery/CreatorGetPreAuthorizationStatusByTtuid` | none | — | Not tested |
| Creator get sparkads auth request by id in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CreatorGetSparkAdsAuthRequestByID` | unwrapped | — | Not tested |
| Creator join campaign for un login in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/CreatorJoinCampaignForUnLogin` | unwrapped | — | Not tested |
| Creator respond linking negotiation in the order query service. | GET | read-only | `/CreativeOne/OrderQuery/CreatorRespondLinkingNegotiation` | params | `linkingRequestID`, `operation`, `orderID` | Not tested |
| Creator search product infos in the order query service. | POST | action-or-mutation | `/CreativeOne/OrderQuery/CreatorSearchProductInfos` | data | `campaignID`, `catalogSkuID`, `catalogSpuID`, `productQuery`, `sortCondition`, `page`, `limit` | Not tested |
| Fetch content suite creator label info in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/FetchContentSuiteCreatorLabelInfo` | unwrapped | — | Not tested |
| Get app list by adv id in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/GetAppListByAdvID` | unwrapped | — | Not tested |
| Get branded effect info in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/GetBrandedEffectInfo` | unwrapped | — | Not tested |
| Get campaign link item random in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/GetCampaignLinkItemRandom` | unwrapped | — | Not tested |
| Get campaign link item records in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/GetCampaignLinkItemRecords` | unwrapped | — | Not tested |
| Get catalog list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/GetCatalogList` | unwrapped | — | Not tested |
| Get client remaining cap in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/GetClientRemainingCap` | unwrapped | — | Not tested |
| Get creator spot in the order query service. | GET | read-only | `/CreativeOne/OrderQuery/GetCreatorSpot` | none | — | Not tested |
| Get keyword suggestions in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/GetKeywordSuggestions` | unwrapped | — | Not tested |
| Get link item creator info in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/GetLinkItemCreatorInfo` | unwrapped | — | Not tested |
| Get product list for campaign in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/GetProductListForCampaign` | unwrapped | — | Not tested |
| Get product list from catalog in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/GetProductListFromCatalog` | unwrapped | — | Not tested |
| Get product set list from catalog in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/GetProductSetListFromCatalog` | unwrapped | — | Not tested |
| Get requirement template in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/GetRequirementTemplate` | unwrapped | — | Not tested |
| Get video url by video id or item id in the order query service. | GET | read-only | `/CreativeOne/OrderQuery/GetVideoUrlByVideoIDOrItemID` | params | `videoID`, `itemID` | Not tested |
| Inner get company by tracking number in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/InnerGetCompanyByTrackingNumber` | unwrapped | — | Not tested |
| Inner mcp get app info from hive in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/InnerMCPGetAppInfoFromHive` | unwrapped | — | Not tested |
| Inner mcp get campaign info in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/InnerMCPGetCampaignInfo` | unwrapped | — | Not tested |
| Inner mcp get creator history finished order cnt in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/InnerMCPGetCreatorHistoryFinishedOrderCnt` | unwrapped | — | Not tested |
| Inner mcp get creator ongoing order cnt in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/InnerMCPGetCreatorOngoingOrderCnt` | unwrapped | — | Not tested |
| Inner mcp get creator recent finished oppo in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/InnerMCPGetCreatorRecentFinishedOppo` | unwrapped | — | Not tested |
| Inner mcp get opportunity info in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/InnerMCPGetOpportunityInfo` | unwrapped | — | Not tested |
| Inner mcp get page info from hive in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/InnerMCPGetPageInfoFromHive` | unwrapped | — | Not tested |
| Inner mcp get product context in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/InnerMCPGetProductContext` | unwrapped | — | Not tested |
| M get content cooperations can send invitation status in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/MGetContentCooperationsCanSendInvitationStatus` | unwrapped | — | Not tested |
| M get product infos from catalog in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/MGetProductInfosFromCatalog` | unwrapped | — | Not tested |
| Multi get campaign has opportunity in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/MultiGetCampaignHasOpportunity` | unwrapped | — | Not tested |
| Multi get campaign has opportunity for partner in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/MultiGetCampaignHasOpportunityForPartner` | unwrapped | — | Not tested |
| Order detail for admin in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/OrderDetailForAdmin` | unwrapped | — | Not tested |
| Partner campaign detail in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerCampaignDetail` | unwrapped | — | Not tested |
| Partner campaign list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerCampaignList` | unwrapped | — | Not tested |
| Partner campaign overview in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerCampaignOverview` | unwrapped | — | Not tested |
| Partner campaign video count in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerCampaignVideoCount` | unwrapped | — | Not tested |
| Partner check apply cancel partner campaign available in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerCheckApplyCancelPartnerCampaignAvailable` | unwrapped | — | Not tested |
| Partner collaboration draft product brief in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerCollaborationDraftProductBrief` | unwrapped | — | Not tested |
| Partner collaboration list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerCollaborationList` | unwrapped | — | Not tested |
| Partner collaboration video list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerCollaborationVideoList` | unwrapped | — | Not tested |
| Partner collaboration video list v2 in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerCollaborationVideoListV2` | unwrapped | — | Not tested |
| Partner get campaign detail in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerGetCampaignDetail` | unwrapped | — | Not tested |
| Partner get campaign fund pool in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerGetCampaignFundPool` | unwrapped | — | Not tested |
| Partner get campaign oac status in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerGetCampaignOacStatus` | unwrapped | — | Not tested |
| Partner get campaign overview in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerGetCampaignOverview` | unwrapped | — | Not tested |
| Partner get collab cnt in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerGetCollabCnt` | unwrapped | — | Not tested |
| Partner get collaboration stage count in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerGetCollaborationStageCount` | unwrapped | — | Not tested |
| Partner get commission summary in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerGetCommissionSummary` | unwrapped | — | Not tested |
| Partner get held budget in orders in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerGetHeldBudgetInOrders` | unwrapped | — | Not tested |
| Partner get invite records in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerGetInviteRecords` | unwrapped | — | Not tested |
| Partner get opportunity detail in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerGetOpportunityDetail` | unwrapped | — | Not tested |
| Partner get order detail in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerGetOrderDetail` | unwrapped | — | Not tested |
| Partner get pe campaign video cnt in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerGetPECampaignVideoCnt` | unwrapped | — | Not tested |
| Partner get partner campaign refund in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerGetPartnerCampaignRefund` | unwrapped | — | Not tested |
| Partner get wish creator list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerGetWishCreatorList` | unwrapped | — | Not tested |
| Partner query drama order video list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerQueryDramaOrderVideoList` | unwrapped | — | Not tested |
| Partner query partner exchange campaign concept in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerQueryPartnerExchangeCampaignConcept` | unwrapped | — | Not tested |
| Partner query partner exchange campaign creative in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerQueryPartnerExchangeCampaignCreative` | unwrapped | — | Not tested |
| Partner query partner exchange campaign item in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerQueryPartnerExchangeCampaignItem` | unwrapped | — | Not tested |
| Partner select creator campaign list in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PartnerSelectCreatorCampaignList` | unwrapped | — | Not tested |
| Premium buzz package info in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/PremiumBuzzPackageInfo` | unwrapped | — | Not tested |
| Query content engine sync log in the order query service. | UNKNOWN | unknown | `/CreativeOne/OrderQuery/QueryContentEngineSyncLog` | unwrapped | — | Not tested |

## Passport (22)

| Action | Method | Classification | Endpoint | Input | Parameters | Live |
| --- | --- | --- | --- | --- | --- | --- |
| Bind employee aio client read relation in the passport service. | UNKNOWN | unknown | `/CreativeOne/Passport/BindEmployeeAIOClientReadRelation` | unwrapped | — | Not tested |
| Bind employee aio client write relation in the passport service. | UNKNOWN | unknown | `/CreativeOne/Passport/BindEmployeeAIOClientWriteRelation` | unwrapped | — | Not tested |
| Cancel login as relation ship in the passport service. | UNKNOWN | unknown | `/CreativeOne/Passport/CancelLoginAsRelationShip` | unwrapped | — | Not tested |
| Client sign protocol in the passport service. | UNKNOWN | unknown | `/CreativeOne/Passport/ClientSignProtocol` | unwrapped | — | Not tested |
| Creative one launch switch in the passport service. | UNKNOWN | unknown | `/CreativeOne/Passport/CreativeOneLaunchSwitch` | unwrapped | — | Not tested |
| Creator account logout in the passport service. | UNKNOWN | unknown | `/CreativeOne/Passport/CreatorAccountLogout` | unwrapped | — | Not tested |
| Creator account new register in the passport service. | UNKNOWN | unknown | `/CreativeOne/Passport/CreatorAccountNewRegister` | unwrapped | — | Not tested |
| Creator account pre register in the passport service. | UNKNOWN | unknown | `/CreativeOne/Passport/CreatorAccountPreRegister` | unwrapped | — | Not tested |
| Creator account real register in the passport service. | UNKNOWN | unknown | `/CreativeOne/Passport/CreatorAccountRealRegister` | unwrapped | — | Not tested |
| Creator account register in the passport service. | UNKNOWN | unknown | `/CreativeOne/Passport/CreatorAccountRegister` | unwrapped | — | Not tested |
| Creator sign protocol in the passport service. | POST | action-or-mutation | `/CreativeOne/Passport/CreatorSignProtocol` | data | `protocolIDS`, `bizFrom`, `source`, `targetType`, `targetID` | Not tested |
| Creator sign protocol by ttu id in the passport service. | POST | action-or-mutation | `/CreativeOne/Passport/CreatorSignProtocolByTTUID` | data | `protocolIDS`, `bizFrom`, `source`, `targetType`, `targetID` | Not tested |
| Get client protocols signature status in the passport service. | UNKNOWN | unknown | `/CreativeOne/Passport/GetClientProtocolsSignatureStatus` | unwrapped | — | Not tested |
| Get creator hacker info in the passport service. | UNKNOWN | unknown | `/CreativeOne/Passport/GetCreatorHackerInfo` | unwrapped | — | Not tested |
| Get creator protocol detail in the passport service. | UNKNOWN | unknown | `/CreativeOne/Passport/GetCreatorProtocolDetail` | unwrapped | — | Not tested |
| Get creator protocol detail info by ttu id in the passport service. | GET | read-only | `/CreativeOne/Passport/GetCreatorProtocolDetailInfoByTTUID` | params | `protocolID` | Not tested |
| Get creator protocols signature status in the passport service. | GET | read-only | `/CreativeOne/Passport/GetCreatorProtocolsSignatureStatus` | params | `groupIDS`, `targetType`, `targetID` | Not tested |
| Get creator protocols signature status by ttu id in the passport service. | UNKNOWN | unknown | `/CreativeOne/Passport/GetCreatorProtocolsSignatureStatusByTTUID` | unwrapped | — | Not tested |
| Get creator protocols signature status v2 in the passport service. | UNKNOWN | unknown | `/CreativeOne/Passport/GetCreatorProtocolsSignatureStatusV2` | unwrapped | — | Not tested |
| Get protocol content by group id and country in the passport service. | UNKNOWN | unknown | `/CreativeOne/Passport/GetProtocolContentByGroupIDAndCountry` | unwrapped | — | Not tested |
| Get protocol content by protocol id in the passport service. | UNKNOWN | unknown | `/CreativeOne/Passport/GetProtocolContentByProtocolID` | unwrapped | — | Not tested |
| Per login check in the passport service. | GET | read-only | `/CreativeOne/Passport/PerLoginCheck` | params | `source`, `groupIDS`, `simpleCheck` | Not tested |

## Payment (9)

| Action | Method | Classification | Endpoint | Input | Parameters | Live |
| --- | --- | --- | --- | --- | --- | --- |
| Exchange currency in the payment service. | GET | read-only | `/CreativeOne/Payment/ExchangeCurrency` | params | `sourceCurrency`, `targetCurrency`, `sourceAmount100k`, `convertTimestamp`, `rateSource` | Not tested |
| Get creator earning detail in the payment service. | GET | read-only | `/CreativeOne/Payment/GetCreatorEarningDetail` | params | `transactionID`, `bizOrderID`, `routingParam` | Not tested |
| Get creator income info in the payment service. | GET | read-only | `/CreativeOne/Payment/GetCreatorIncomeInfo` | params | `needBalance`, `needDetail` | Not tested |
| Get creator monthly amount in the payment service. | GET | read-only | `/CreativeOne/Payment/GetCreatorMonthlyAmount` | params | `cTzOffset`, `transactionType`, `transactionSource`, `startTime`, `endTime` | Not tested |
| Get creator payment config in the payment service. | GET | read-only | `/CreativeOne/Payment/GetCreatorPaymentConfig` | params | `routingParam` | Not tested |
| Get creator transaction account url in the payment service. | GET | read-only | `/CreativeOne/Payment/GetCreatorTransactionAccountURL` | none | — | Not tested |
| Get creator transaction list in the payment service. | GET | read-only | `/CreativeOne/Payment/GetCreatorTransactionList` | params | `transactionType`, `transactionSource`, `startTime`, `endTime`, `limit`, `page` | Not tested |
| Get creator withdraw detail in the payment service. | GET | read-only | `/CreativeOne/Payment/GetCreatorWithdrawDetail` | params | `transactionID` | Not tested |
| Get creator withdraw url in the payment service. | GET | read-only | `/CreativeOne/Payment/GetCreatorWithdrawURL` | params | `cAid`, `ttLanguage`, `deviceID` | Not tested |

## Report (34)

| Action | Method | Classification | Endpoint | Input | Parameters | Live |
| --- | --- | --- | --- | --- | --- | --- |
| Admin get traffic diagnosis info in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/AdminGetTrafficDiagnosisInfo` | unwrapped | — | Not tested |
| Create or update custom report in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/CreateOrUpdateCustomReport` | unwrapped | — | Not tested |
| Creative center get top contents item detail in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/CreativeCenterGetTopContentsItemDetail` | unwrapped | — | Not tested |
| Creative center get top contents list in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/CreativeCenterGetTopContentsList` | unwrapped | — | Not tested |
| Creator get top contents list in the report service. | GET | read-only | `/CreativeOne/Report/CreatorGetTopContentsList` | params | `periodDimension`, `periodEndTimestamp`, `orderByMetric`, `countryCode`, `contentLabelIDs`, `organicOnly`, `limit`, `page` | Not tested |
| Creator get video perf data in the report service. | GET | read-only | `/CreativeOne/Report/CreatorGetVideoPerfData` | params | `orderID`, `videoID`, `itemID` | Not tested |
| Delete custom report in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/DeleteCustomReport` | unwrapped | — | Not tested |
| Download report result in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/DownloadReportResult` | unwrapped | — | Not tested |
| Get anchor report info in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetAnchorReportInfo` | unwrapped | — | Not tested |
| Get audience distribution in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetAudienceDistribution` | unwrapped | — | Not tested |
| Get campaign country report in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetCampaignCountryReport` | unwrapped | — | Not tested |
| Get campaign report ads perf trend in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetCampaignReportAdsPerfTrend` | unwrapped | — | Not tested |
| Get campaign report detail in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetCampaignReportDetail` | unwrapped | — | Not tested |
| Get campaign report engagement trend in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetCampaignReportEngagementTrend` | unwrapped | — | Not tested |
| Get campaign report list in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetCampaignReportList` | unwrapped | — | Not tested |
| Get campaign report overview trend in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetCampaignReportOverviewTrend` | unwrapped | — | Not tested |
| Get campaign report video performance trend in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetCampaignReportVideoPerformanceTrend` | unwrapped | — | Not tested |
| Get campaign v region in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetCampaignVRegion` | unwrapped | — | Not tested |
| Get custom report settings in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetCustomReportSettings` | unwrapped | — | Not tested |
| Get download resource in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetDownloadResource` | unwrapped | — | Not tested |
| Get entity report detail in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetEntityReportDetail` | unwrapped | — | Not tested |
| Get entity report list in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetEntityReportList` | unwrapped | — | Not tested |
| Get gtm top contents item detail in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetGTMTopContentsItemDetail` | unwrapped | — | Not tested |
| Get gtm top contents list in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetGTMTopContentsList` | unwrapped | — | Not tested |
| Get item report detail in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetItemReportDetail` | unwrapped | — | Not tested |
| Get local audience distribution in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetLocalAudienceDistribution` | unwrapped | — | Not tested |
| Get optimization suggestions in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetOptimizationSuggestions` | unwrapped | — | Not tested |
| Get top contents item detail in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetTopContentsItemDetail` | unwrapped | — | Not tested |
| Get top contents list in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetTopContentsList` | unwrapped | — | Not tested |
| Get top contents overview in the report service. | GET | read-only | `/CreativeOne/Report/GetTopContentsOverview` | none | — | Not tested |
| Get video report list in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/GetVideoReportList` | unwrapped | — | Not tested |
| Sharable unified query in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/SharableUnifiedQuery` | unwrapped | — | Not tested |
| Toggle video shortlist status in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/ToggleVideoShortlistStatus` | unwrapped | — | Not tested |
| Unified query in the report service. | UNKNOWN | unknown | `/CreativeOne/Report/UnifiedQuery` | unwrapped | — | Not tested |
