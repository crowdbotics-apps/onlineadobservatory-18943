from django.urls import path

from . import views


urlpatterns = [
    path(  # Total Spend by Page of Region
        'total_spend/by_page/of_region/<slug:region_name>',
        views.TotalSpendByPageOfRegion.as_view()
    ),
    path(  # Total Spend of Page of Region
        'total_spend/of_page/<int:page_id>/of_region/<slug:region_name>',
        views.TotalSpendOfPageOfRegion.as_view()
    ),
    path(  # Spend by Time Period of Page of Region
        'spend_by_time_period/of_page/<int:page_id>/of_region/<slug:region_name>',
        views.SpendByTimePeriodOfPageOfRegion.as_view()
    ),
    path(  # Total Spend by Page of Topic of Region
        'total_spend/by_page/of_topic/<slug:topic_name>/of_region/<slug:region_name>',
        views.TotalSpendByTopicOfRegion.as_view()
    ),
    path(  # Total Spend by Topic of Region
        'total_spend/by_topic/of_region/<slug:region_name>',
        views.TotalSpendByTopicOfRegion.as_view()
    ),
    path(  # Spend by Time Period by Topic of Page
        'spend_by_time_period/by_topic/of_page/<int:page_id>',
        views.SpendByTimePeriodByTopicOfPage.as_view()
    ),
    path(  # Spend by Time Period of Topic of Region
        'spend_by_time_period/of_topic/<slug:topic_name>/of_region/<slug:region_name>',
        views.SpendByTimePeriodOfTopicOfRegion.as_view()
    ),
    path(  # Total Spend by Purpose of Page
        'total_spend/by_purpose/of_page/<int:page_id>',
        views.TotalSpendByPurposeOfPage.as_view()
    ),
    path(  # Total Spend by Purpose of Region
        'total_spend/by_purpose/of_region/<slug:region_name>',
        views.TotalSpendByPurposeOfRegion.as_view()
    ),
    path(  # Spend by Targeting of Region - Dummy data 7/14, live data 7/25
        'total_spend/by_targeting/of_region/<slug:region_name>',
        views.SpendByTargetingOfPage.as_view()
    ),
    path(  # Spend by Targeting of Page - Dummy data 7/14, live data 7/25
        'total_spend/by_targeting/of_page/<int:page_id>',
        views.SpendByTargetingOfPage.as_view()
    ),
    path(  # Percentage of Targeting Seen of Page
        'targeting/of_page/<int:page_id>',
        views.PercentageOfTargetingSeenOfPage.as_view()
    ),
    path(  # search
        'getads',
        views.GetAds.as_view()
    ),
    path(
        'getaddetails/<int:ad_cluster_id>',
        views.GetAddDetais.as_view()
    ),
    path(
        'archive-id/<int:archive_id>/cluster',
        views.ArchiveId.as_view()
    ),
    path(  # Topics
        'topics',
        views.Topics.as_view()
    ),
    path(  # Races
        'races',
        views.Races.as_view()
    ),
    path(  # Candidates in a race
        'race/<int:race_id>/candidates',
        views.CandidatesInARace.as_view()
    ),
    path(  # Search Pages by type
        'search/pages_type_ahead',
        views.SearchPagesTypeAhead.as_view()
    ),
    path(  # Autocomplete Funding Entities
        'autocomplete/fun ding_entities',
        views.AutocompleteFundingEntities.as_view()
    ),
    path(  # Get Notifications
        'notifications/of_user/<slug:email>',
        views.GetNotifications.as_view()
    ),
    path(  # Add Notification
        'notifications/add',
        views.AddNotification.as_view()
    ),
    path(  # Remove Notification
        'notifications/remove/<int:notification_id>',
        views.RemoveNotification.as_view()
    )
]
