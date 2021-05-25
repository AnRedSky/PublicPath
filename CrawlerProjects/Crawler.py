import requests
from lxml import etree

# import matplotlib.pyplot as mlt
# import seaborn as sns


url = 'https://www.timeshighereducation.com/world-university-rankings/2021/world-ranking#!/page/0/length/25/sort_by/name/sort_order/asc/cols/stats'

headers = {
    'user-agent': ' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

response = requests.get(url, headers).text

text = '''
    <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en" dir="ltr"
    xmlns:og="http://ogp.me/ns#">
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" lang="en" />
    <script></script>
    <link href="https://www.timeshighereducation.com/world-university-rankings/2021/world-ranking?site=cn" rel="alternate" hreflang="en" />
    <link href="https://www.timeshighereducation.com/cn/world-university-rankings/2021/world-ranking?site=cn" rel="alternate" hreflang="zh-hans" />
    <link rel="alternate" href="https://www.timeshighereducation.com/world-university-rankings/2021/world-ranking" hreflang="X-default" />
    <meta name="atdlayout" content="section" />
    <link rel="shortcut icon" href="https://www.timeshighereducation.com/sites/default/themes/custom/the_responsive/favicon.ico" type="image/vnd.microsoft.icon" />
    <script src="https://go.automatad.com/geo/ktlyva/afihbs.js" async=""></script>
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:site" content="@timeshighered" />
    <meta name="twitter:title" content="World University Rankings 2021" />
    <meta name="twitter:image" content="https://www.timeshighereducation.com/sites/default/themes/custom/the_responsive/img/social/ranking-dataset-share.jpg" />
    <meta baidu-gxt-verify-token="264dee6caa2e44b18a2ebf9ed11b782b" />
    <script type="application/ld+json">{
        "@context": "http://schema.org",
        "@graph": [
            {
                "publisher": {
                    "@type": "Organization",
                    "@id": "https://www.timeshighereducation.com",
                    "name": "Times Higher Education (THE)",
                    "url": "https://www.timeshighereducation.com",
                    "logo": {
                        "@type": "ImageObject",
                        "url": "https://www.timeshighereducation.com/sites/default/themes/custom/the_responsive/img/logo/logo-wur-2x.png",
                        "width": "612px",
                        "height": "200px"
                    }
                },
                "@type": "WebSite",
                "@id": "https://www.timeshighereducation.com",
                "name": "Times Higher Education (THE)",
                "url": "https://www.timeshighereducation.com"
            }
        ]
    }</script>
    <meta name="description" content="The Times Higher Education World University Rankings 2021 include more than 1,500 universities across 93 countries and regions, making them the largest and most diverse university rankings to date. The table is based on 13 carefully calibrated performance indicators that measure an institution’s performance across four areas: teaching, research, knowledge transfer and" />
    <link rel="canonical" href="https://www.timeshighereducation.com/world-university-rankings/2021/world-ranking" />
    <link rel="shortlink" href="https://www.timeshighereducation.com/node/698687" />
    <meta property="mz:id" content="698687" />
    <meta property="og:site_name" content="Times Higher Education (THE)" />
    <meta property="mz:section" content="rankings" />
    <meta property="og:type" content="article" />
    <meta property="mz:subsection" content="World University Rankings" />
    <meta property="og:url" content="https://www.timeshighereducation.com/world-university-rankings/2021/world-ranking" />
    <meta property="mz:type" content="rankings_table" />
    <meta property="mz:language" content="en" />
    <meta property="og:title" content="World University Rankings" />
    <meta property="og:description" content="The Times Higher Education World University Rankings 2021 include more than 1,500 universities across 93 countries and regions, making them the largest and most diverse university rankings to date." />
    <meta property="mz:pagename" content="World University Rankings 2021" />
    <meta property="og:updated_time" content="2020-09-07T10:03:27+01:00" />
    <meta property="og:image" content="https://www.timeshighereducation.com/sites/default/themes/custom/the_responsive/img/social/ranking-dataset-share.jpg" />
    <meta property="og:image:type" content="image/jpeg" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta property="article:published_time" content="2020-08-25T16:33:00+01:00" />
    <meta property="article:modified_time" content="2020-09-07T10:03:27+01:00" />
    <meta name="msvalidate.01" content="DBA2827FABEE1B561280B9DBAD77C9A3" />
    <meta name="google-site-verification" content="KJs1E-IVyjYA-caTRM8z_rMaVUI_xI-lHuRXCAqu4Zo" />
    <title>World University Rankings 2021 | Times Higher Education (THE)</title>
    <link type="text/css" rel="stylesheet" href="https://www.timeshighereducation.com/sites/default/files/css/css_lQaZfjVpwP_oGNqdtWCSpJT1EMqXdMiU84ekLLxQnc4.css" media="all" />
    <link type="text/css" rel="stylesheet" href="https://www.timeshighereducation.com/sites/default/files/css/css_pwToiYNH15skcTltS8NaDup2ATHVvVW3DZbiB6EqpfA.css" media="all" />
    <link type="text/css" rel="stylesheet" href="https://www.timeshighereducation.com/sites/default/files/css/css_6P1x7N0zTep8vAoOekKGsXSYOODJhERBOtjf_mbpOC4.css" media="all" />
    <link type="text/css" rel="stylesheet" href="https://www.timeshighereducation.com/sites/default/files/css/css_uhG_pruzURU743NtYQb2bhJziyqavN0gyvYTISvSdoo.css" media="all" />
    <link type="text/css" rel="stylesheet" href="https://www.timeshighereducation.com/sites/default/files/css/css_kzjR6CQNAH520oBgsgQejhPIc1i6g5IgKEfUJ92Vw48.css" media="all" />
    <script>
        (function(w){w._mz = {};w._mz_def=[];_mz.emit=function(t,d,n){w._mz_def.push({f:'emit',t:t,d:d,n:n});};}(window));
    </script>
    <script src="https://www.timeshighereducation.com/sites/default/files/js/js_bbCGLpSpp4w_Z4tkp3SAkgA1j9E1mUPxKVfCBVwMQhE.js"></script>
    <script src="https://www.timeshighereducation.com/sites/default/files/js/js_3e7YIephLzZ2tVFlbN3w0P9cLZu4Hg_KeJ-Qxn_hS84.js"></script>
    <script src="https://www.timeshighereducation.com/sites/default/files/js/js_BYWhgsfEEfLAOBJlz3hnovlv1646DHBB3VH_au0t_Og.js"></script>
    <script src="https://www.timeshighereducation.com/sites/default/files/js/js_FeWeF0BMmV25woOXGjSXIIe2nFBkinfC7fJ8kOW815A.js"></script>
    <script>window.eu_cookie_compliance_cookie_name = "";</script>
    <script src="https://www.timeshighereducation.com/sites/default/files/js/js_mP9bhHhQ8BXZzGrbTLCXVOYA_982U_c-j2-ynPHqJo4.js"></script>
    <script src="https://www.timeshighereducation.com/sites/default/files/js/js_HLPhb-4bikD-LUuPzbETxbQEEcA_-TOZ5n-OJjnyYLY.js"></script>
    <script>jQuery.extend(Drupal.settings, {"basePath":"\/","pathPrefix":"","ajaxPageState":{"theme":"the_responsive","theme_token":"YzFwFC7_hnfttqqO0cdwIxkg8V_eEU9RoTLdkgGhFpU","jquery_version":"1.7","js":{"misc\/jquery.once.js":1,"sites\/default\/modules\/custom\/the_data_rankings\/includes\/the_data_rankings.js":1,"sites\/default\/modules\/custom\/the_geography_extras\/js\/the-geography-extras.js":1,"sites\/default\/modules\/custom\/the_data_rankings\/includes\/the_data_rankings_jump.js":1,"sites\/default\/modules\/custom\/mz_events_the\/js\/mz_events_the.js":1,"sites\/default\/modules\/custom\/the_login_modal\/js\/the_login_modal.js":1,"sites\/default\/themes\/custom\/the_responsive\/js\/hacks.js":1,"sites\/default\/themes\/custom\/the_responsive\/js\/nav-main.js":1,"sites\/all\/libraries\/jssocials\/jssocials.min.js":1,"sites\/default\/modules\/shared\/mz_analytics\/js\/mz_analytics.js":1,"sites\/default\/modules\/custom\/the_nag_footer\/includes\/the_nag_footer.js":1,"sites\/all\/modules\/contrib\/chosen\/chosen.js":1,"0":1,"sites\/all\/themes\/contrib\/bootstrap\/js\/bootstrap.js":1,"sites\/default\/modules\/custom\/the_student_registration\/js\/the_student_wall_nag.js":1,"sites\/all\/modules\/contrib\/jquery_update\/replace\/jquery\/1.7\/jquery.min.js":1,"misc\/jquery-extend-3.4.0.js":1,"misc\/jquery-html-prefilter-3.5.0-backport.js":1,"misc\/drupal.js":1,"sites\/all\/libraries\/fontfaceobserver\/fontfaceobserver.js":1,"sites\/default\/themes\/custom\/the_responsive\/js\/font-loader.js":1,"sites\/all\/modules\/contrib\/jquery_update\/replace\/ui\/ui\/minified\/jquery.ui.core.min.js":1,"sites\/all\/libraries\/stickybits\/dist\/stickybits.min.js":1,"sites\/all\/libraries\/chosen\/chosen.jquery.min.js":1,"sites\/all\/libraries\/datatables\/media\/js\/jquery.dataTables.min.js":1,"sites\/all\/libraries\/datatables\/media\/js\/dataTables.bootstrap.min.js":1,"sites\/all\/modules\/contrib\/eu_cookie_compliance\/js\/jquery.cookie-1.4.1.min.js":1,"sites\/all\/modules\/contrib\/jquery_update\/replace\/jquery.form\/4\/jquery.form.min.js":1,"misc\/ajax.js":1,"sites\/all\/modules\/contrib\/jquery_update\/js\/jquery_update.js":1,"sites\/default\/modules\/custom\/the_user_registration\/js\/the_user_registration_mz_events.js":1,"sites\/default\/themes\/custom\/the_responsive\/js\/global.js":1,"sites\/default\/modules\/custom\/the_uni_apply\/includes\/the_uni_apply_rankings_cta_buttons.js":1,"sites\/default\/modules\/custom\/the_uni_apply\/includes\/the_uni_apply_rankings.js":1,"sites\/default\/modules\/custom\/the_jobs\/js\/the_jobs.js":1,"sites\/default\/modules\/custom\/the_traffic_drivers\/includes\/the_traffic_drivers.js":1,"sites\/all\/themes\/contrib\/bootstrap\/js\/misc\/_progress.js":1,"sites\/all\/modules\/contrib\/ctools\/js\/modal.js":1,"sites\/default\/modules\/custom\/the_login_modal\/js\/the-login-modal-theme.js":1,"sites\/all\/modules\/contrib\/ctools\/js\/ajax-responder.js":1,"sites\/default\/modules\/custom\/the_ads\/js\/the_ads.js":1,"sites\/default\/modules\/custom\/the_ums_modal\/js\/the_ums_modal_close.js":1,"sites\/default\/modules\/custom\/the_ums_modal\/js\/the-ums-modal-theme.js":1,"1":1,"sites\/all\/modules\/contrib\/eu_cookie_compliance\/js\/eu_cookie_compliance.js":1,"sites\/default\/modules\/shared\/the_cache_control\/the_cache_control_new_relic.js":1,"sites\/all\/libraries\/smartmenus\/jquery.smartmenus.min.js":1,"sites\/all\/libraries\/smartmenus\/addons\/bootstrap\/jquery.smartmenus.bootstrap.min.js":1,"sites\/all\/libraries\/readmore\/readmore.min.js":1,"sites\/default\/themes\/custom\/the_responsive\/js\/nav-sub.js":1,"sites\/all\/libraries\/bootstrap\/dist\/js\/bootstrap.min.js":1,"sites\/default\/themes\/custom\/the_responsive\/js\/custom-popover.js":1,"sites\/all\/themes\/contrib\/bootstrap\/js\/modules\/ctools\/js\/modal.js":1,"sites\/all\/themes\/contrib\/bootstrap\/js\/misc\/ajax.js":1},"css":{"modules\/system\/system.base.css":1,"sites\/all\/libraries\/chosen\/chosen.css":1,"sites\/all\/modules\/contrib\/chosen\/css\/chosen-drupal.css":1,"sites\/all\/libraries\/datatables\/media\/css\/dataTables.bootstrap.min.css":1,"sites\/all\/libraries\/datatables\/media\/css\/responsive.dataTables.css":1,"misc\/ui\/jquery.ui.core.css":1,"misc\/ui\/jquery.ui.theme.css":1,"modules\/field\/theme\/field.css":1,"modules\/node\/node.css":1,"sites\/default\/modules\/custom\/the_user_restrictions\/css\/paywall_message.css":1,"sites\/all\/modules\/contrib\/workflow\/workflow_admin_ui\/workflow_admin_ui.css":1,"sites\/all\/modules\/contrib\/views\/css\/views.css":1,"sites\/all\/modules\/contrib\/ctools\/css\/ctools.css":1,"sites\/default\/modules\/custom\/the_panels_bootstrap_layouts\/plugins\/layouts\/bootstrap_bricks\/..\/the-panels-bootstrap-layouts.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__content_header_primary.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__content_header_primary_rankings.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__content_header_secondary.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/element__ranking_sponsor.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/page__us_rankings.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__sentence_style_form.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__sentence_style_form_ranking_overrides.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__profile_key_statistics.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__rankings_datatables_overrides.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__rankings_jump_select_box.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__rankings_pagination.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__rankings_regional_table.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__rankings_responsive_table.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__rankings_social_links.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__social_academic.css":1,"sites\/all\/modules\/contrib\/panels\/plugins\/layouts\/onecol\/onecol.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/view_display__articles_rankings_sidebar.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__jobs_list.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__traffic_driver.css":1,"sites\/all\/modules\/contrib\/ctools\/css\/modal.css":1,"sites\/default\/modules\/custom\/the_ads\/css\/the_ads.css":1,"modules\/locale\/locale.css":1,"sites\/all\/modules\/contrib\/node_embed\/plugins\/node_embed\/node_embed.css":1,"sites\/all\/modules\/contrib\/eu_cookie_compliance\/css\/eu_cookie_compliance.bare.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__search_form.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__search_form_institution.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__search_form_keywords.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__search_form_page.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/page__rankings.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__social_share_simple.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/element__link__country_flag.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__profile_driver.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__pairwise_comparison.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__reg-survey.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__user_login_register_forms.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__sdg_components.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__article_byline.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__streetbees_info.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__is_new_label.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__box.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__product_teaser.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__ott_checkbox.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__custom-hybridauth-widget.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__student_guide_nag.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__student_wall.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__menu_grid.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/element__date.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/element__more_link.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/layout__the_main_with_sidebar.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/layout__the_article_layout.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/layout__the_landing_page.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/form__corporate_subscriber_weblead.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/form__mailchimp_newsletters.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/form__registration.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/page__subscription_signup.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/utilities__display.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/vendor\/bootstrap-sass\/bootstrap_styles.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/base__font-declarations.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/vendor\/jssocial\/jssocial_styles.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/base__overrides_bootstrap.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/base__overrides_drupal.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/base__overrides_recurly.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/base__typography_extras.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/base__colours.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__nav_primary.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__nav_primary_mobile.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__nav_primary_buttons.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__nav_secondary.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__nav_secondary_user_menu.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__nav_sticky.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__sub_nav_sticky.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__modals.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__ums-buttons.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__footer.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__nag_footer.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__student-ctas.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__resubscribe.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__wur_lists_basket.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__wur_modal.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__wur_my_lists.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__wur_universities_list.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__sliding_popup.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__inline-navigation.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/paragraph__all.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/element__breadcrumb_header.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/element__adverts.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/element__title.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/element__social_fonts.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/element__headings.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/element__buttons.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/element__read_more.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/element__label.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/element__video.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/element__article_image.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/block__language_locale.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/block__recurly_currency_switcher.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/layout__panel_regions.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/layout__main_container.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__legacy_miscellaneous.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__legacy_views.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__legacy_taxomony_term_item.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/the_pane_style.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__teaser_card.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__teaser_card_horizontal.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/component__article_teaser_feature_half_width.css":1,"sites\/default\/themes\/custom\/the_responsive\/css\/styles\/layout__views.css":1}},"chosen":{"selector":"select:not(#edit-pages):visible","minimum_single":20,"minimum_multiple":20,"minimum_width":200,"options":{"allow_single_deselect":false,"disable_search":false,"disable_search_threshold":0,"search_contains":true,"placeholder_text_multiple":"Choose some options","placeholder_text_single":"Choose an option","no_results_text":"No results match","inherit_select_classes":true}},"urlIsAjaxTrusted":{"\/world-university-rankings\/2021\/world-ranking?site=cn":true,"\/":true},"the_data_rankings":{"#datatable-1":{"columns":[{"data":"rank_order","name":"rank order","class":"rank-order","visible":false,"searchable":false},{"data":"rank","name":"Rank","class":"rank","visible":true,"searchable":false,"orderable":true,"orderData":[0,2],"orderSequence":["asc","desc"]},{"data":"name","name":"Name\u003Cbr \/\u003ECountry\/Region","class":"name namesearch","visible":true,"searchable":true,"orderSequence":["asc","desc"]},{"data":"nid","name":"Node ID","class":"nid","visible":false,"searchable":false},{"data":"scores_overall","name":"Overall","class":"scores overall-score","visible":false,"orderable":true,"orderData":[5],"searchable":false},{"data":"scores_overall_rank","name":"","class":"never","visible":false,"searchable":false,"orderSequence":["asc","desc"]},{"data":"scores_teaching","name":"Teaching","class":"scores teaching-score","visible":false,"orderable":true,"orderData":[7],"searchable":false},{"data":"scores_teaching_rank","name":"","class":"never","visible":false,"searchable":false,"orderSequence":["asc","desc"]},{"data":"scores_research","name":"Research","class":"scores research-score","visible":false,"orderable":true,"orderData":[9],"searchable":false},{"data":"scores_research_rank","name":"","class":"never","visible":false,"searchable":false,"orderSequence":["asc","desc"]},{"data":"scores_citations","name":"Citations","class":"scores citations-score","visible":false,"orderable":true,"orderData":[11],"searchable":false},{"data":"scores_citations_rank","name":"","class":"never","visible":false,"searchable":false,"orderSequence":["asc","desc"]},{"data":"scores_industry_income","name":"Industry Income","class":"scores industry_income-score","visible":false,"orderable":true,"orderData":[13],"searchable":false},{"data":"scores_industry_income_rank","name":"","class":"never","visible":false,"searchable":false,"orderSequence":["asc","desc"]},{"data":"scores_international_outlook","name":"International Outlook","class":"scores international_outlook-score","visible":false,"orderable":true,"orderData":[15],"searchable":false},{"data":"scores_international_outlook_rank","name":"","class":"never","visible":false,"searchable":false,"orderSequence":["asc","desc"]},{"data":"record_type","name":"","class":"never","visible":false,"searchable":false},{"data":"member_level","name":"","class":"never","visible":false,"searchable":false},{"data":"url","name":"","class":"never","visible":false,"searchable":false},{"data":"location","name":"","class":"never","visible":false,"searchable":true},{"data":"aliases","name":"","class":"never namesearch","visible":false,"searchable":true},{"data":"subjects_offered","name":"","class":"never","visible":false,"searchable":true},{"data":"stats_number_students","name":"No. of FTE Students","class":"stats stats_number_students","visible":true,"searchable":false,"orderSequence":["desc","asc"],"type":"num-fmt"},{"data":"stats_student_staff_ratio","name":"No. of students per staff","class":"stats stats_student_staff_ratio","visible":true,"searchable":false,"orderSequence":["desc","asc"],"type":"num-fmt"},{"data":"stats_pc_intl_students","name":"International Students","class":"stats stats_pc_intl_students","visible":true,"searchable":false,"orderSequence":["desc","asc"],"type":"num-fmt"},{"data":"stats_female_male_ratio","name":"Female:Male Ratio","class":"stats stats_female_male_ratio","visible":true,"searchable":false,"orderSequence":["desc","asc"],"type":"string"}],"ajax":{"cache":true,"url":"https:\/\/www.timeshighereducation.com\/sites\/default\/files\/the_data_rankings\/world_university_rankings_2021_0__fa224219a267a5b9c4287386a97c70ea.json","dataSrc":"data"},"dom":"rtilp","searching":1,"pageLength":25,"lengthChange":1,"stateSave":0,"deferRender":true,"paging":true,"bootstrap":true,"responsive":{"details":false},"autoWidth":false,"nid":"698687","language":{"url":"\/sites\/default\/modules\/custom\/the_data_rankings\/i18n\/datatables_en.json"},"order":[1,"asc"],"lengthMenu":[[10,25,50,100,-1],[10,25,50,100,"All"]],"year":"2021","rank_type":"world_university_rankings"}},"the_uni_apply":{"apply_text":"Enquire"},"the_dfp":{"slots":[],"enable_debug":0,"disable_initial_load":1,"enable_lazyload":1,"lazyload_fetchMarginPercent":"100","lazyload_renderMarginPercent":"90","lazyload_mobileScaling":"2","enable_autorefresh":0,"autorefresh_time":"23000","keyvalues":{"5041ad8f9ee4d1807669fa7f2f32de34":{"nid":"698687"}}},"the_jobs":{"the_jobs_debug":null},"theImpressionsTracking":{"impressions":{"job":[254143,254074,254101,254098,254139],"ranking_institution":["697918","648719","699792","623262"]}},"CToolsModal":{"loadingText":"Loading...","closeText":"Close Window","closeImage":"\u003Cimg class=\u0022img-responsive\u0022 src=\u0022https:\/\/www.timeshighereducation.com\/sites\/all\/modules\/contrib\/ctools\/images\/icon-close-window.png\u0022 alt=\u0022Close window\u0022 title=\u0022Close window\u0022 \/\u003E","throbber":"\u003Cimg class=\u0022img-responsive\u0022 src=\u0022https:\/\/www.timeshighereducation.com\/sites\/all\/modules\/contrib\/ctools\/images\/throbber.gif\u0022 alt=\u0022Loading\u0022 title=\u0022Loading...\u0022 \/\u003E"},"the-modal-style":{"modalSize":{"type":"scale","width":"1","height":"1"},"modalOptions":{"opacity":0.5,"background-color":"#000"},"animation":"fadeIn","modalTheme":"THELoginModal","closeText":""},"the-ums-modal-style-xxlarge":{"modalSize":{"type":"scale","width":"1","height":"1"},"modalOptions":{"opacity":0.5,"background-color":"#000"},"animation":"fadeIn","modalTheme":"THEUMSModalThemeXxlarge","closeText":"X"},"the-ums-modal-style-xlarge":{"modalSize":{"type":"scale","width":"1","height":"1"},"modalOptions":{"opacity":0.5,"background-color":"#000"},"animation":"fadeIn","modalTheme":"THEUMSModalThemeXlarge","closeText":"X"},"the_ads":{"endpoint":"https:\/\/www.timeshighereducation.com\/cps\/api\/the_ads"},"eu_cookie_compliance":{"cookie_policy_version":"1.0.0","popup_enabled":1,"popup_agreed_enabled":0,"popup_hide_agreed":0,"popup_clicking_confirmation":0,"popup_scrolling_confirmation":0,"popup_html_info":"\u003Cdiv class=\u0022eu-cookie-compliance-banner eu-cookie-compliance-banner-info eu-cookie-compliance-banner--default\u0022\u003E\n  \u003Cdiv class=\u0022popup-content info\u0022\u003E\n    \u003Cdiv id=\u0022popup-text\u0022\u003E\n      \u003Cp\u003EBy using the THE website you agree to our use of cookies as described in our \u003Ca href=\u0022\/cookie-policy\u0022 target=\u0022_blank\u0022 rel=\u0022noopener noreferrer\u0022\u003Ecookie policy\u003C\/a\u003E.\u003C\/p\u003E          \u003C\/div\u003E\n    \n    \u003Cdiv id=\u0022popup-buttons\u0022 class=\u0022\u0022\u003E\n      \u003Cbutton type=\u0022button\u0022 class=\u0022agree-button eu-cookie-compliance-default-button\u0022\u003EOK\u003C\/button\u003E\n          \u003C\/div\u003E\n  \u003C\/div\u003E\n\u003C\/div\u003E","use_mobile_message":false,"mobile_popup_html_info":"\u003Cdiv class=\u0022eu-cookie-compliance-banner eu-cookie-compliance-banner-info eu-cookie-compliance-banner--default\u0022\u003E\n  \u003Cdiv class=\u0022popup-content info\u0022\u003E\n    \u003Cdiv id=\u0022popup-text\u0022\u003E\n                \u003C\/div\u003E\n    \n    \u003Cdiv id=\u0022popup-buttons\u0022 class=\u0022\u0022\u003E\n      \u003Cbutton type=\u0022button\u0022 class=\u0022agree-button eu-cookie-compliance-default-button\u0022\u003EOK\u003C\/button\u003E\n          \u003C\/div\u003E\n  \u003C\/div\u003E\n\u003C\/div\u003E\n","mobile_breakpoint":"768","popup_html_agreed":"\u003Cdiv\u003E\n  \u003Cdiv class=\u0022popup-content agreed\u0022\u003E\n    \u003Cdiv id=\u0022popup-text\u0022\u003E\n      \u003Cp\u003E\u0026lt;h2\u0026gt;Thank you for accepting cookies\u0026lt;\/h2\u0026gt;\u0026lt;p\u0026gt;You can now hide this message or find out more about cookies.\u0026lt;\/p\u0026gt;\u003C\/p\u003E\n    \u003C\/div\u003E\n    \u003Cdiv id=\u0022popup-buttons\u0022\u003E\n      \u003Cbutton type=\u0022button\u0022 class=\u0022hide-popup-button eu-cookie-compliance-hide-button\u0022\u003EHide\u003C\/button\u003E\n          \u003C\/div\u003E\n  \u003C\/div\u003E\n\u003C\/div\u003E","popup_use_bare_css":1,"popup_height":"auto","popup_width":0,"popup_delay":1000,"popup_link":"\/cookie-policy","popup_link_new_window":1,"popup_position":true,"fixed_top_position":false,"popup_language":"en","store_consent":false,"better_support_for_screen_readers":0,"reload_page":0,"domain":"","domain_all_sites":0,"popup_eu_only_js":0,"cookie_lifetime":"100","cookie_session":false,"disagree_do_not_show_popup":0,"method":"default","allowed_cookies":"","withdraw_markup":"\u003Cbutton type=\u0022button\u0022 class=\u0022eu-cookie-withdraw-tab\u0022\u003EPrivacy settings\u003C\/button\u003E\n\u003Cdiv class=\u0022eu-cookie-withdraw-banner\u0022\u003E\n  \u003Cdiv class=\u0022popup-content info\u0022\u003E\n    \u003Cdiv id=\u0022popup-text\u0022\u003E\n      \u003Cp\u003E\u0026lt;h2\u0026gt;We use cookies on this site to enhance your user experience\u0026lt;\/h2\u0026gt;\u0026lt;p\u0026gt;You have given your consent for us to set cookies.\u0026lt;\/p\u0026gt;\u003C\/p\u003E\n    \u003C\/div\u003E\n    \u003Cdiv id=\u0022popup-buttons\u0022\u003E\n      \u003Cbutton type=\u0022button\u0022 class=\u0022eu-cookie-withdraw-button\u0022\u003EWithdraw consent\u003C\/button\u003E\n    \u003C\/div\u003E\n  \u003C\/div\u003E\n\u003C\/div\u003E\n","withdraw_enabled":false,"withdraw_button_on_info_popup":0,"cookie_categories":[],"cookie_categories_details":[],"enable_save_preferences_button":1,"cookie_name":"","containing_element":"body","automatic_cookies_removal":true},"thenf":{"start":"400","min_width":"1080","restrict_roles":0,"roles":{"1":0,"2":0,"3":0,"4":0,"5":0,"30":0,"8":0,"13":0,"10":0,"19":0,"25":0,"28":0,"36":0,"42":0},"restrict_languages":1,"languages":{"en":"en","zh-hans":0,"fr":0}},"mz_variables":{"mz_script":"\/\/www.timeshighereducation.com\/cdn\/mz\/7928895\/mz.js","user_variables":{"id":0},"mz_domain":"","mz_events_separate":"","page_variables":{"version":209,"app":"academic","variant":"drupal","thirdPartyAnalyticsDisabled":true,"thirdPartyGoogleAnalytics":[{"trackingId":"UA-35881683-9","trackingName":"student","customDimensions":[{"dimensionIndex":"1","dimensionValue":""},{"dimensionIndex":"2","dimensionValue":false}]}]},"admin_tracking":0},"the_user":[],"bootstrap":{"anchorsFix":0,"anchorsSmoothScrolling":1,"formHasError":1,"popoverEnabled":0,"popoverOptions":{"animation":1,"html":0,"placement":"right","selector":"","trigger":"click","triggerAutoclose":1,"title":"","content":"","delay":0,"container":"body"},"tooltipEnabled":0,"tooltipOptions":{"animation":1,"html":0,"placement":"auto left","selector":"","trigger":"hover focus","delay":0,"container":"body"}}});</script>
    </head>
    <body class="html not-front not-logged-in no-sidebars page-node page-node- page-node-698687 node-type-ranking-dataset i18n-en font-loader wur-logo"  data-nid="698687">
    <div class="white-modal"></div>
    <div id="skip-link">
        <a href="#main-content" class="element-invisible element-focusable">Skip to main content</a>
    </div>
        

    <header id="navbar" role="banner" class="navbar navbar-default navbar-white js-sticky-nav">
    <div class="container">
        <div class="row">
        <div class="col-sm-12">
            <!-- Primary Mobile Navbar Header -->
            <div class="navbar-header">
            <!-- Menu button -->
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#main-menu" aria-expanded="false">Menu</button>
            <!-- Logo -->
                        <div class="navbar-btn--wrapper">
                <a data-mz data-module="site_logo" class="logo navbar-btn" href="/" title="Home">Times Higher Education</a>
                </div>
                        <!-- Site name -->
                        <a class="name navbar-brand" href="/" title="Home">Times Higher Education (THE)</a>
                    </div>

            <!-- Primary Desktop Navbar Header -->
                    <div class="navbar-collapse collapse" id="main-menu">

                <!-- Desktop & Mobile Primary Nav List -->
                <nav role="navigation" data-module="main-menu">
                                <ul class="menu nav navbar-nav"><li class="first expanded dropdown"><a href="/" title="" data-mz="" data-position="menu" data-target="#" class="dropdown-toggle">Professional</a><ul class="dropdown-menu"><li class="first leaf"><a href="/news" data-mz="" data-position="menu">News</a></li>
    <li class="leaf"><a href="/academic/opinion" title="" data-mz="" data-position="menu">Opinion</a></li>
    <li class="leaf"><a href="/comment/reader-comments" title="" data-mz="" data-position="menu">Reader Comments</a></li>
    <li class="leaf"><a href="/academic/books" data-mz="" data-position="menu">Books</a></li>
    <li class="leaf"><a href="/academic/features" data-mz="" data-position="menu">Features</a></li>
    <li class="leaf"><a href="/academic/research" title="" data-mz="" data-position="menu">Research</a></li>
    <li class="last leaf"><a href="/academic/digital-editions" title="" data-mz="" data-position="menu">Digital Editions</a></li>
    </ul></li>
    <li class="expanded dropdown"><a href="https://www.timeshighereducation.com/campus" title="" data-mz="" data-position="menu" data-target="#" class="dropdown-toggle">Campus</a><ul class="dropdown-menu"><li class="first leaf"><a href="https://www.timeshighereducation.com/campus/about-campus" title="" data-mz="" data-position="menu">About Campus</a></li>
    <li class="leaf"><a href="https://www.timeshighereducation.com/campus/collections" title="" data-mz="" data-position="menu">Collections</a></li>
    <li class="leaf"><a href="https://www.timeshighereducation.com/campus/series" title="" data-mz="" data-position="menu">Series</a></li>
    <li class="last leaf"><a href="https://www.timeshighereducation.com/campus/topics" title="" data-mz="" data-position="menu">Topics</a></li>
    </ul></li>
    <li class="expanded dropdown"><a href="https://www.timeshighereducation.com/unijobs" title="" data-mz="" data-position="menu" data-target="#" class="dropdown-toggle">Jobs</a><ul class="dropdown-menu"><li class="first leaf"><a href="https://www.timeshighereducation.com/unijobs/listings/" title="" data-mz="" data-position="menu">Find a job</a></li>
    <li class="leaf"><a href="https://www.timeshighereducation.com/unijobs/newalert/" title="" data-mz="" data-position="menu">Jobs by email</a></li>
    <li class="leaf"><a href="https://www.timeshighereducation.com/unijobs/employers/" title="" data-mz="" data-position="menu">Search recruiters</a></li>
    <li class="last leaf"><a href="/careers" title="" data-mz="" data-position="menu">Careers</a></li>
    </ul></li>
    <li class="expanded dropdown"><a href="/events" title="" data-mz="" data-position="menu" data-target="#" class="dropdown-toggle">Events</a><ul class="dropdown-menu"><li class="first leaf"><a href="/events" title="" data-mz="" data-position="menu">All Events</a></li>
    <li class="leaf"><a href="/events/summits" title="" data-mz="" data-position="menu">Summits</a></li>
    <li class="leaf"><a href="/events/forums" title="" data-mz="" data-position="menu">Forums</a></li>
    <li class="leaf"><a href="/events/webinars" title="" data-mz="" data-position="menu">Webinars</a></li>
    <li class="leaf"><a href="/events/awards" title="" data-mz="" data-position="menu">Awards</a></li>
    <li class="last leaf"><a href="/events/the-live" title="" data-mz="" data-position="menu">THE Live</a></li>
    </ul></li>
    <li class="expanded active-trail active dropdown"><a href="/world-university-rankings" title="" class="active-trail dropdown-toggle" data-mz="" data-position="menu" data-target="#">Rankings</a><ul class="dropdown-menu"><li class="first leaf active-trail active active"><a href="/world-university-rankings/2021/world-ranking" title="" class="active-trail active" data-mz="" data-position="menu">World University Rankings</a></li>
    <li class="leaf"><a href="/impactrankings" data-mz="" data-position="menu">Impact Rankings</a></li>
    <li class="leaf"><a href="/rankings/japan-university/2021" title="" data-mz="" data-position="menu">Japan University Rankings</a></li>
    <li class="leaf"><a href="/rankings/united-states/2021" data-mz="" data-position="menu">US College Rankings</a></li>
    <li class="leaf"><a href="/world-university-rankings/by-subject" title="" data-mz="" data-position="menu">By subject</a></li>
    <li class="leaf"><a href="/policy/rankings" title="" data-mz="" data-position="menu">News</a></li>
    <li class="last leaf"><a href="/world-university-rankings/about-the-times-higher-education-world-university-rankings" title="" data-mz="" data-position="menu">About THE&#039;s rankings</a></li>
    </ul></li>
    <li class="expanded dropdown"><a href="/student" title="" data-mz="" data-position="menu" data-target="#" class="dropdown-toggle">Student</a><ul class="dropdown-menu"><li class="first leaf"><a href="/student/where-to-start" title="" data-mz="" data-position="menu">Where to start</a></li>
    <li class="leaf"><a href="/student/best-universities" title="" data-mz="" data-position="menu">Best universities</a></li>
    <li class="leaf"><a href="/student/student-life" title="" data-mz="" data-position="menu">Student life</a></li>
    <li class="leaf"><a href="/student/how-to-apply" title="" data-mz="" data-position="menu">How to apply</a></li>
    <li class="leaf"><a href="/student/before-you-go" title="" data-mz="" data-position="menu">Before you go</a></li>
    <li class="leaf"><a href="/student/events" title="" data-mz="" data-position="menu">Student events</a></li>
    <li class="last leaf"><a href="/student/student-panel" title="" data-mz="" data-position="menu">Student surveys</a></li>
    </ul></li>
    <li class="last collapsed"><a href="/about-us" title="" data-mz="" data-position="menu">Services</a></li>
    </ul>                                        </nav>
            </div>
            <div class="navbar-button__wrapper">
                <ul class="navbar-buttons"><li class="navbar-buttons__btn"><a href="javascript:void(0)" data-target="block-the-social-links-share-buttons" class="navbar-buttons__btn-link navbar-buttons__btn-link--share js-navbar-buttons__btn-link" title="Share"></a></li>
    <li class="navbar-buttons__btn"><a href="javascript:void(0)" data-target="block-the-login-modal-the-login-modal-multistep" class="btn-toggle--user js-toggle-user navbar-buttons__btn-link navbar-buttons__btn-link--user js-navbar-buttons__btn-link user-anon" title="User account"></a></li>
    <li class="navbar-buttons__btn"><a href="javascript:void(0)" data-target="block-the-site-search-tsskeyword" class="btn-toggle--search navbar-buttons__btn-link navbar-buttons__btn-link--search js-navbar-buttons__btn-link" title="Search"></a></li>
    </ul>          </div>
                </div>

        <!-- Secondary Navigation -->
                <div class="region region-secondary-navigation">
        <section id="block-the-login-modal-the-login-modal-multistep" class="block block-the-login-modal clearfix">

        
    <div class="user-menu">
        <button type="button" class="close js-navbar-buttons__btn-link"
                data-target="block-the-login-modal-the-login-modal-multistep"
                data-dismiss="modal" aria-hidden="true">&times;
        </button>
    <div class="user-menu__user-state user-menu__user-state anonymous">
                    <div>
        <div class="user-menu__message-wrapper">
            <div class="user-menu__message">
                                        </div>
        </div>
        </div>
    </div>
        <ul class="navbar-login-visible user-menu__logged-out-menu">
            <li><a href="/the-ums-modal/login/nojs" id="modal-login" class="ctools-use-modal  ctools-modal-the-ums-modal-style-xlarge">Login</a></li>
            <li><a href="/the-ums-modal/register/nojs" id="modal-register" class="ctools-use-modal  ctools-modal-the-ums-modal-style-xxlarge">Register</a></li>
            <li><a href="/store" data-mz="">Subscribe</a></li>
        </ul>

    </div>

    </section>
    <section id="block-the-site-search-tsskeyword" class="block block-the-site-search clearfix">

        
    <form class="the-search-form the-search-form--keyword" action="/world-university-rankings/2021/world-ranking?site=cn" method="post" id="the-site-search-form-keyword" accept-charset="UTF-8"><div><div class="form-item form-item-keys form-type-textfield form-group"><input title="Search" placeholder="Search" class="search-form__textfield search-keys-field form-control form-text" type="text" id="edit-keys" name="keys" value="" size="60" maxlength="128" /></div><input type="hidden" name="form_build_id" value="form-AfwDyf7oYl0WnIWRbqB1ALCsYdBySUB3BpHdYsDvmo8" />
    <input type="hidden" name="form_id" value="the_site_search_form_keyword" />
    <button type="submit" id="edit-submit--2" name="op" value="GO" class="btn btn-default form-submit form-submit">GO</button>
    </div></form>
    </section>
    <section id="block-the-social-links-share-buttons" class="block block-the-social-links clearfix">

        
    <ul class="soc share-buttons js-share-buttons"><li><a href="http://service.weibo.com/share/share.php?url=https://www.timeshighereducation.com/world-university-rankings/2021/world-ranking&amp;title=World University Rankings 2021" class="weibo" title="Share on weibo" target="_blank" data-network="weibo">Share on weibo</a></li>
    </ul>
    </section>
    </div>
            </div>
    </div>
    </header>

        <div class="region region-hero">
        </div>



    <div class="main-container">

    <header role="banner" id="page-header">
        
        <div class="region region-header">
        <section id="block-the-dfp-the-dfp-header" class="block block-the-dfp clearfix">

        
    <div id="div-gpt-ad-104438158644926-2" data-ad-page="world-university-rankings" data-ad-unit="21841059662/THE_COM/world-university-rankings/table" data-ad-mobile-size="[[300,50],[320,50],[300,100]]" data-ad-size="[970,250]" data-ad-priority="high" data-ad-position="the_dfp_header" data-ad-limit="1" data-ad-key-values="5041ad8f9ee4d1807669fa7f2f32de34" class="the-dfp"></div>

    </section>
    </div>
    </header> <!-- /#page-header -->

        
        
        <a id="main-content"></a>

                                    <div class="region region-content">
        <section id="block-system-main" class="block block-system clearfix">

        
    <div class="layout-bootstrap-override" >
        <div class="content--header__primary">
        <div class="container">
            <div class="row">
            <div class="col-sm-12">
                <div class="panel-pane pane-the-data-rankings-body-header-text"  >
    
        
    
    <div class="pane-content">
        <h1 class="pane-title">World University Rankings 2021</h1><div class="row"><div class="seo-description__wrapper"><div class="seo-description" data-js-read-more="paragraphs-2"><p>The <em>Times Higher Education </em>World University Rankings 2021 include more than 1,500 universities across 93 countries and regions, making them the largest and most diverse university rankings to date.</p>
    <p>The table is based on 13 carefully calibrated performance indicators that measure an institution’s performance across four areas: teaching, research, knowledge transfer and international outlook.</p>
    <p>This year’s ranking analysed more than 80 million citations across over 13 million research publications and included survey responses from 22,000 scholars globally.</p>
    <p>Trusted worldwide by students, teachers, governments and industry experts, this year’s league table provides great insight into the shifting balance of power in global higher education.</p>
    <hr /><p><strong><a href="https://www.timeshighereducation.com/world-university-rankings/world-university-rankings-2021-methodology">View the World University Rankings 2021 methodology</a></strong></p>
    <hr /><p>The University of Oxford tops the rankings for the fifth consecutive year, while mainland China’s Tsinghua University becomes the first Asian university to break into the top 20 under the current methodology (launched in 2011).</p>
    <p>The US claims a record eight places in the top 10, after the University of California, Berkeley climbed six places to seventh, but US universities outside the top 200 show signs of decline.</p>
    <p>Meanwhile, there are 141 first-time entrants in the rankings this year, topped by France’s recently merged Paris-Saclay University (joint 178<sup>th</sup>). India has the highest number of new entries (14) and as a result boasts a record number of ranked institutions (63).</p>
    <hr /><p><strong><a href="https://www.timeshighereducation.com/world-university-rankings/how-worlds-top-universities-have-been-impacted-covid-19">Read our analysis of the <em>THE</em> World University Rankings 2021 results</a></strong></p>
    <p><a href="https://www.timeshighereducation.com/digital-editions/world-university-rankings-2021-digital-edition"><strong>Download a free copy of the World University Rankings 2021 digital supplement</strong></a></p>
    <p><strong>To raise your university’s global profile with <em>Times Higher Education</em>, please contact <a href="mailto:branding@timeshighereducation.com">branding@timeshighereducation.com</a></strong></p>
    <p><strong>To unlock the data behind <em>THE</em>’s rankings and access a range of analytical and benchmarking tools, </strong><a href="https://mailchi.mp/timeshighereducation.com/datapoints#utm_source=THEwebsite&amp;utm_medium=WUR_table_header&amp;utm_campaign=data_points_CTA">click here</a></p></div></div><div class="data-source-controls__wrapper"><div class="data-source-controls"><div class="data-source-controls__dataset-source__wrapper elsevier"><div class="data-source-controls__dataset-source elsevier year-2021"></div></div></div><select id="edit-jump"><option selected="selected" value="/world-university-rankings/2021/world-ranking">2021</option><option value="/world-university-rankings/2020/world-ranking">2020</option><option value="/world-university-rankings/2019/world-ranking">2019</option><option value="/world-university-rankings/2018/world-ranking">2018</option><option value="/world-university-rankings/2017/world-ranking">2017</option><option value="/world-university-rankings/2016/world-ranking">2016</option><option value="/world-university-rankings/2015/world-ranking">2015</option><option value="/world-university-rankings/2014/world-ranking">2014</option><option value="/world-university-rankings/2013/world-ranking">2013</option><option value="/world-university-rankings/2012/world-ranking">2012</option><option value="/world-university-rankings/2011/world-ranking">2011</option></select><a class="btn btn-primary" data-mz="" href="/submitting-data-times-higher-education-2020-world-university-rankings">How to get your uni ranked</a></div></div>  </div>

    
    </div>
            </div>
            </div>
        </div>
        </div>
            <div class="content--header__secondary">
        <div class="container">
            <div class="row">
            <div class="col-sm-12">
                <div class="panel-pane pane-the-data-rankings-sentence-form"  >
    
        
    
    <div class="pane-content">
        <form action="/world-university-rankings/2021/world-ranking?site=cn" method="post" id="the-data-rankings-sentence-form" accept-charset="UTF-8"><div><div class="search-form--sentence-style"><div class="search-form--sentence-style--sentence-1"><div class="form-item form-item-pillars form-type-select form-group"> <label class="control-label" for="pillars"><span id="first-word">Show</span> me universities best for </label>
    <select class="form-control form-select" id="pillars" name="pillars"></select></div><div class="form-item form-item-location form-type-select form-group"> <label class="control-label" for="location"> in </label>
    <select multiple="" data-placeholder="any country / region" placeholder="any country / region" class="form-control form-select" id="location" name="location"><option value="0">any country / region</option></select></div><div class="form-item form-item-subjects form-type-select form-group"> <label class="control-label" for="subjects"> offering </label>
    <select class="form-control form-select" id="subjects" name="subjects"><option value="0">any subject</option></select></div></div><div class="search-form--sentence-style--sentence-2"><div class="form-item form-item-name form-type-textfield form-group"> <label class="control-label" for="edit-name">Or, find specific universities </label>
    <input placeholder="by name" name="name" class="form-control form-control form-text" type="text" id="edit-name" value="" size="30" maxlength="128" /></div></div></div><input type="hidden" name="form_build_id" value="form-h8EmRmae4f40FsGpfcoP-94lUkj7Sy9y_M3KDBxvKBY" />
    <input type="hidden" name="form_id" value="the_data_rankings_sentence_form" />
    </div></form>  </div>

    
    </div>
            </div>
            </div>
        </div>
        </div>
        <div class="container">
                    <div class="row">
        <div class="col-sm-8 content-primary">
            <div class="panel-pane pane-the-data-rankings-datatables"  >
    
        
    
    <div class="pane-content">
        <table id ="datatable-1" class="table"><thead><tr><th class="rank-order">rank order</th><th class="rank">Rank</th><th class="name namesearch">Name<br />Country/Region</th><th class="nid">Node ID</th><th class="scores overall-score" title="The overall score" data-placement="top" data-toggle="tooltip"><div class="rotate">Overall</div></th><th class="never"></th><th class="scores teaching-score" title="" data-placement="top" data-toggle="tooltip"><div class="rotate">Teaching</div></th><th class="never"></th><th class="scores research-score" title="" data-placement="top" data-toggle="tooltip"><div class="rotate">Research</div></th><th class="never"></th><th class="scores citations-score" title="" data-placement="top" data-toggle="tooltip"><div class="rotate">Citations</div></th><th class="never"></th><th class="scores industry_income-score" title="" data-placement="top" data-toggle="tooltip"><div class="rotate">Industry Income</div></th><th class="never"></th><th class="scores international_outlook-score" title="" data-placement="top" data-toggle="tooltip"><div class="rotate">International Outlook</div></th><th class="never"></th><th class="never"></th><th class="never"></th><th class="never"></th><th class="never"></th><th class="never namesearch"></th><th class="never"></th><th class="stats stats_number_students"><div class="rotate">No. of FTE Students</div></th><th class="stats stats_student_staff_ratio"><div class="rotate">No. of students per staff</div></th><th class="stats stats_pc_intl_students"><div class="rotate">International Students</div></th><th class="stats stats_female_male_ratio"><div class="rotate">Female:Male Ratio</div></th></tr></thead><tbody></tbody></table>  </div>

    
    </div>
    <div class="panel-separator"></div><div class="panel-pane pane-social-links"  >
    
        
    
    <div class="pane-content">
        <ul class="soc share-buttons js-share-buttons"><li><a href="https://twitter.com/intent/tweet?url=https://www.timeshighereducation.com/world-university-rankings/2021/world-ranking&amp;via=timeshighered&amp;text=World University Rankings 2021" class="twitter" title="Share on twitter" target="_blank" data-network="twitter">Share on twitter</a></li>
    <li><a href="https://www.facebook.com/sharer/sharer.php?u=https://www.timeshighereducation.com/world-university-rankings/2021/world-ranking&amp;p[title]=World University Rankings 2021" class="facebook" title="Share on facebook" target="_blank" data-network="facebook">Share on facebook</a></li>
    <li><a href="https://www.linkedin.com/shareArticle?url=https://www.timeshighereducation.com/world-university-rankings/2021/world-ranking&amp;title=World University Rankings 2021" class="linkedin" title="Share on linkedin" target="_blank" data-network="linkedin">Share on linkedin</a></li>
    <li><a href="mailto:?subject=Check out World University Rankings 2021&amp;body= View it here https://www.timeshighereducation.com/world-university-rankings/2021/world-ranking&amp;url=https://www.timeshighereducation.com/world-university-rankings/2021/world-ranking&amp;title=World University Rankings 2021" class="mail" title="Share on mail" target="_blank" data-network="mail">Share on mail</a></li>
    </ul>  </div>

    
    </div>
    <div class="panel-separator"></div><div class="panel-pane pane-entity-field pane-node-field-rankings-disclaimer"  >
    
        
    
    <div class="pane-content">
        <div class="field field-name-field-rankings-disclaimer field-type-node-reference field-label-hidden"><div class="field-items"><div class="field-item even"><a href="/world-university-rankings-2021-table-information">World University Rankings 2021 table information</a></div></div></div>  </div>

    
    </div>
                                    <div class="row">
                            <div class="col-sm-6">
                <div class="panel-pane pane-hub-traffic-drivers"  >
    
        
    
    <div class="pane-content">
        <div class="traffic-driver-container"></div>
    </div>

    
    </div>
                </div>
                                        <div class="col-sm-6">
                <div class="panel-pane pane-hub-traffic-drivers"  >
    
        
    
    <div class="pane-content">
        <div class="traffic-driver-container"></div>
    </div>

    
    </div>
                </div>
                        </div>
                        </div>
        <div class="col-sm-4 sidebar-primary sidebar-primary--right">
            <div class="panel-pane pane-panels-mini pane-right-sidebar-rankings"  >
    
            <h3 class="pane-title">
        Read more about the World University Rankings 2021    </h3>
        
    
    <div class="pane-content">
        <div class="panel-display panel-1col clearfix" id="mini-panel-right_sidebar_rankings">
    <div class="panel-panel panel-col">
        <div><div class="panel-pane pane-views-panes pane-rankings-linked-articles-panel-pane-2"  >
    
        
    
    <div class="pane-content">
        <div data-module="rankings_linked_articles-panel_pane_2" class="view view-rankings-linked-articles view-id-rankings_linked_articles view-display-id-panel_pane_2 view-dom-id-42df5326112b61a9ecae977416177f87">
            
    
    
        <div class="view-content">
            <div class="views-row views-row-1 views-row-odd views-row-first views-row-last">      
    <div class="views-field views-field-field-student-rankings-insights">    <h4 class="views-label views-label-field-student-rankings-insights">Student Insights</h4>    <div class="field-content"><ul><li><a data-mz data-position="list" href="/student/best-universities/best-universities-world">Best universities in the world</a></li>
    <li><a data-mz data-position="list" href="/student/best-universities/best-universities-uk">Best universities in the UK</a></li>
    <li><a data-mz data-position="list" href="/student/best-universities/best-universities-united-states">Best universities in the United States</a></li>
    <li><a data-mz data-position="list" href="/student/best-universities/best-universities-canada">Best universities in Canada</a></li>
    <li><a data-mz data-position="list" href="/student/best-universities/best-universities-germany">Best universities in Germany</a></li>
    <li><a data-mz data-position="list" href="/student/best-universities/best-universities-france">Best universities in France</a></li>
    <li><a data-mz data-position="list" href="/student/best-universities/best-universities-netherlands">Best universities in the Netherlands</a></li>
    <li><a data-mz data-position="list" href="/student/best-universities/best-universities-australia">Best universities in Australia</a></li>
    <li><a data-mz data-position="list" href="/student/best-universities/best-universities-china">Best universities in China</a></li>
    <li><a data-mz data-position="list" href="/student/best-universities/best-universities-europe">Best universities in Europe</a></li>
    <li><a data-mz data-position="list" href="/student/best-universities/best-universities-china">Best universities in China</a></li>
    <li><a data-mz data-position="list" href="/student/best-universities/best-universities-spain">Best universities in Spain</a></li>
    </ul></div>  </div>  </div>    </div>
    
    
    
    
    
    
    </div>  </div>

    
    </div>
    <div class="panel-separator"></div><div class="panel-pane pane-views-panes pane-rankings-linked-articles-panel-pane-1"  >
    
        
    
    <div class="pane-content">
        <div data-module="rankings_linked_articles-panel_pane_1" class="view view-rankings-linked-articles view-id-rankings_linked_articles view-display-id-panel_pane_1 view-dom-id-c64190f8d7c986c0a8e2734a511eb32a">
            
    
    
        <div class="view-content">
            <div class="views-row views-row-1 views-row-odd views-row-first views-row-last">      
    <div class="views-field views-field-field-academic-rankings-insights">    <h4 class="views-label views-label-field-academic-rankings-insights">Academic Insights</h4>    <div class="field-content"><ul><li><a data-mz data-position="list" href="/news/world-university-rankings-2021-results-announced">THE World University Rankings 2021: results announced</a></li>
    <li><a data-mz data-position="list" href="/world-university-rankings/world-university-rankings-2021-people-power-needed-never">THE World University Rankings 2021: people power needed like never before</a></li>
    <li><a data-mz data-position="list" href="/world-university-rankings/how-worlds-top-universities-have-been-impacted-covid-19">How the world’s top universities have been impacted by Covid-19</a></li>
    <li><a data-mz data-position="list" href="/opinion/us-public-universities-must-be-properly-supported-ward-next-crisis">US public universities must be properly supported to ward off the next crisis</a></li>
    <li><a data-mz data-position="list" href="/world-university-rankings/world-university-rankings-2021-china-closing-us">THE World University Rankings 2021: China closing in on the US </a></li>
    <li><a data-mz data-position="list" href="/world-university-rankings/will-covid-19-lead-more-equitable-research-links">Will Covid-19 lead to more equitable research links?</a></li>
    <li><a data-mz data-position="list" href="/world-university-rankings/world-university-rankings-2021-international-student-flows">THE World University Rankings 2021: international student flows</a></li>
    <li><a data-mz data-position="list" href="/world-university-rankings/world-university-rankings-2021-how-research-impact-changing">THE World University Rankings 2021: how research impact is changing</a></li>
    <li><a data-mz data-position="list" href="/world-university-rankings/world-university-rankings-2021-teaching-post-covid-world">THE World University Rankings 2021: teaching in a post-Covid world</a></li>
    <li><a data-mz data-position="list" href="/opinion/pandemic-does-not-spell-end-residential-education">The pandemic does not spell the end for residential education</a></li>
    <li><a data-mz data-position="list" href="/world-university-rankings/world-university-rankings-2021-how-covid-19-changing-research">THE World University Rankings 2021: how Covid-19 is changing research</a></li>
    <li><a data-mz data-position="list" href="/opinion/we-must-use-pandemic-build-more-sustainable-research-system">We must use the pandemic to build a more sustainable research system</a></li>
    <li><a data-mz data-position="list" href="/world-university-rankings/world-university-rankings-2021-korean-universities-find-strength-their">THE World University Rankings 2021: Korean universities find strength in their industry roots </a></li>
    <li><a data-mz data-position="list" href="/opinion/covid-19-chance-create-new-model-knowledge-transfer">Covid-19 is a chance to create a new model of knowledge transfer </a></li>
    <li><a data-mz data-position="list" href="/world-university-rankings/world-university-rankings-2021-internationalisation-post-covid-world">THE World University Rankings 2021: internationalisation in a post-Covid world</a></li>
    <li><a data-mz data-position="list" href="/opinion/universities-must-remain-international-after-pandemic">Universities must remain international after the pandemic</a></li>
    <li><a data-mz data-position="list" href="/opinion/higher-education-needs-new-model-global-partnerships">Higher education needs a new model for global partnerships </a></li>
    <li><a data-mz data-position="list" href="/opinion/universities-and-society-will-only-recover-covid-19-through-civic-engagement">Universities and society will only recover from Covid-19 through civic engagement </a></li>
    <li><a data-mz data-position="list" href="/world-university-rankings/its-brave-new-wur">It’s a brave new WUR </a></li>
    </ul></div>  </div>  </div>    </div>
    
    
    
    
    
    
    </div>  </div>

    
    </div>
    <div class="panel-separator"></div><div class="panel-pane pane-views-panes pane-rankings-linked-articles-panel-pane-3"  >
    
        
    
    <div class="pane-content">
        <div data-module="rankings_linked_articles-panel_pane_3" class="view view-rankings-linked-articles view-id-rankings_linked_articles view-display-id-panel_pane_3 view-dom-id-49a330d5958a8f4a30cccb96bf1f20b5">
            
    
    
        <div class="view-content">
            <div class="views-row views-row-1 views-row-odd views-row-first views-row-last">      
    <div class="views-field views-field-title-field">    <h4 class="views-label views-label-title-field">Methodology: </h4>    <div class="field-content"><a data-mz data-position="list" href="/world-university-rankings/world-university-rankings-2021-methodology">THE World University Rankings 2021: methodology</a></div>  </div>  </div>    </div>
    
    
    
    
    
    
    </div>  </div>

    
    </div>
    <div class="panel-separator"></div><div class="panel-pane pane-custom pane-1"  >
    
        
    
    <div class="pane-content">
        <p><a href="https://timeshighereducation,com/student"><img alt="Link through to the new THE Student platform" class="media-element file-wysiwyg img-responsive" data-delta="3" src="https://www.timeshighereducation.com/sites/default/files/styles/article785xauto/public/the-student-homepage-cta-mobile.jpg?itok=Ml_0BJuS" width="785" height="1097" /></a></p>  </div>

    
    </div>
    <div class="panel-separator"></div><div class="panel-pane pane-the-dfp-advert"  >
    
        
    
    <div class="pane-content">
        <div data-ad-page="world-university-rankings" class="the-dfp" id="div-gpt-ad-438994001607491-1" data-ad-unit="21841059662/THE_COM/world-university-rankings/table" data-ad-priority="high" data-ad-size="[[300,600],[300,250]]" data-ad-mobile-size="[[300,600],[300,250]]"></div>
    </div>

    
    </div>
    <div class="panel-separator"></div><div class="panel-pane pane-the-jobs"  >
    
            <h2 class="pane-title">
        Featured jobs    </h2>
        
    
    <div class="pane-content">
        <div class="job-listings" data-module="the-jobs">
    <div class="job-listing">
        <img class="job-listing__recruiter-logo" src="//d311j2r2qvjkvi.cloudfront.net/getasset/d962a838-d887-43ad-92b0-5a122117d7dd/" alt="Recruiter logo" />
        <h3 class="job-listing__title">
        <a href="//www.timeshighereducation.com/unijobs/listing/254143/?trackid=10" data-position="1" data-mz="">Associate Professor in Marketing </a>    </h3>
        <div class="job-listing__recruiter-name">Edinburgh Napier University</div>
    </div>
    <div class="job-listing">
        <img class="job-listing__recruiter-logo" src="//d311j2r2qvjkvi.cloudfront.net/getasset/edd46e36-83d5-4718-8c0a-88a99fb94445/" alt="Recruiter logo" />
        <h3 class="job-listing__title">
        <a href="//www.timeshighereducation.com/unijobs/listing/254074/?trackid=10" data-position="2" data-mz="">Lecturer in Information Systems</a>    </h3>
        <div class="job-listing__recruiter-name">Cranfield University</div>
    </div>
    <div class="job-listing">
        <img class="job-listing__recruiter-logo" src="//d311j2r2qvjkvi.cloudfront.net/getasset/7e421a17-d434-4a1b-af2b-112664238ff9/" alt="Recruiter logo" />
        <h3 class="job-listing__title">
        <a href="//www.timeshighereducation.com/unijobs/listing/254101/?trackid=10" data-position="3" data-mz="">Clinical Psychologist</a>    </h3>
        <div class="job-listing__recruiter-name">University Of Southampton</div>
    </div>
    <div class="job-listing">
        <img class="job-listing__recruiter-logo" src="//d311j2r2qvjkvi.cloudfront.net/getasset/cb9c01dc-4a81-47e5-8c96-7630a6945d7d/" alt="Recruiter logo" />
        <h3 class="job-listing__title">
        <a href="//www.timeshighereducation.com/unijobs/listing/254098/?trackid=10" data-position="4" data-mz="">Senior Lecturer in Adult Nursing</a>    </h3>
        <div class="job-listing__recruiter-name">University Of Lincoln</div>
    </div>
    <div class="job-listing">
        <img class="job-listing__recruiter-logo" src="//d311j2r2qvjkvi.cloudfront.net/getasset/2fbdfe3e-048e-46ee-b378-abefdc41d627/" alt="Recruiter logo" />
        <h3 class="job-listing__title">
        <a href="//www.timeshighereducation.com/unijobs/listing/254139/?trackid=10" data-position="5" data-mz="">Research Associate, Department of Infectious Diseases</a>    </h3>
        <div class="job-listing__recruiter-name">Kings College London</div>
    </div>
    </div>
    <div class="job-see-more">
    <a href="//www.timeshighereducation.com/unijobs/listings/" class="btn btn-primary btn-sm" data-mz="">See all jobs</a>  </div>
    </div>

    
    </div>
    <div class="panel-separator"></div><div class="panel-pane pane-hub-traffic-drivers"  >
    
        
    
    <div class="pane-content">
        <div class="traffic-driver-container"></div>
    </div>

    
    </div>
    </div>
    </div>
    </div>
    </div>

    
    </div>
    <div class="panel-separator"></div><div class="panel-pane pane-profile-trafic-drivers"  >
    
            <h2 class="pane-title">
        Featured universities    </h2>
        
    
    <div class="pane-content">
        <div id="node-697918" class="node node-ranking-institution node-profile_driver member-silver-student-focus has-logo member-silver-student-focus clearfix" data-module="profile-driver">
    <div class="profile-driver">
            <div class="profile-driver__banner-image">
            <a href="/world-university-rankings/university-canada-west" data-mz data-position="driver-image">
            <img class="img-responsive" src="https://www.timeshighereducation.com/sites/default/files/styles/large/public/institution/header_image/img1950x700.jpg?itok=JmAE46HI" alt="" title="" />        </a>
        </div>
            <div class="profile-driver__content">
                <div class="profile-driver__logo">
            <a href="/world-university-rankings/university-canada-west" data-mz data-position="driver-logo">
                <img class="img-responsive" src="https://www.timeshighereducation.com/sites/default/files/styles/medium/public/ucw_logo-400x400.jpg?itok=GzxjoqDs" alt="" title="" />          </a>
            </div>
                <div class="profile-driver__links--wrapper">
                    <h3 class="profile-driver__title"><a href="/world-university-rankings/university-canada-west" data-mz data-position="driver-title">University Canada West</a></h3>
                            <div class="profile-driver__ctas"><div class="profile-driver__button"><div class="field field-name-field-institution-video field-type-media field-label-hidden"><div class="field-items"><div class="field-item even"><a class="profile-driver__button-icon btn btn-default btn-xs btn-margin" href="/world-university-rankings/university-canada-west?popupvideo=true">Video</a></div></div></div></div>
    <div class="profile-driver__button"><a href="/world-university-rankings/university-canada-west" class="btn btn-default btn-xs" data-mz="">Explore</a></div>
    </div>              </div>
        </div>
    </div>
    </div>
    <div id="node-648719" class="node node-ranking-institution node-profile_driver member-silver has-logo member-silver clearfix" data-module="profile-driver">
    <div class="profile-driver">
            <div class="profile-driver__banner-image">
            <a href="/world-university-rankings/federation-university-australia" data-mz data-position="driver-image">
            <img class="img-responsive" src="https://www.timeshighereducation.com/sites/default/files/styles/large/public/institution/header_image/the_federation_university_hero_image.png?itok=B1dUdLKb" alt="" title="" />        </a>
        </div>
            <div class="profile-driver__content">
                <div class="profile-driver__logo">
            <a href="/world-university-rankings/federation-university-australia" data-mz data-position="driver-logo">
                <img class="img-responsive" src="https://www.timeshighereducation.com/sites/default/files/styles/medium/public/fed150yc_black_400x400.png?itok=h6xle6B6" alt="" title="" />          </a>
            </div>
                <div class="profile-driver__links--wrapper">
                    <h3 class="profile-driver__title"><a href="/world-university-rankings/federation-university-australia" data-mz data-position="driver-title">Federation University Australia</a></h3>
                            <div class="profile-driver__ctas"><div class="profile-driver__button"><div class="field field-name-field-institution-video field-type-media field-label-hidden"><div class="field-items"><div class="field-item even"><a class="profile-driver__button-icon btn btn-default btn-xs btn-margin" href="/world-university-rankings/federation-university-australia?popupvideo=true">Video</a></div></div></div></div>
    <div class="profile-driver__button"><a href="/world-university-rankings/federation-university-australia" class="btn btn-default btn-xs" data-mz="">Explore</a></div>
    </div>              </div>
        </div>
    </div>
    </div>
    <div id="node-699792" class="node node-ranking-institution node-profile_driver member-silver has-logo member-silver clearfix" data-module="profile-driver">
    <div class="profile-driver">
            <div class="profile-driver__banner-image">
            <a href="/world-university-rankings/arden-university" data-mz data-position="driver-image">
            <img class="img-responsive" src="https://www.timeshighereducation.com/sites/default/files/styles/large/public/institution/header_image/arden-affiliate-times-higher-education-img-2.jpg?itok=5xCMgkm9" alt="" title="" />        </a>
        </div>
            <div class="profile-driver__content">
                <div class="profile-driver__logo">
            <a href="/world-university-rankings/arden-university" data-mz data-position="driver-logo">
                <img class="img-responsive" src="https://www.timeshighereducation.com/sites/default/files/styles/medium/public/arden-affiliate-times-higher-education-logo.png?itok=MZa6NT6P" alt="" title="" />          </a>
            </div>
                <div class="profile-driver__links--wrapper">
                    <h3 class="profile-driver__title"><a href="/world-university-rankings/arden-university" data-mz data-position="driver-title">Arden University</a></h3>
                            <div class="profile-driver__ctas"><div class="profile-driver__button"><div class="field field-name-field-institution-video field-type-media field-label-hidden"><div class="field-items"><div class="field-item even"><a class="profile-driver__button-icon btn btn-default btn-xs btn-margin" href="/world-university-rankings/arden-university?popupvideo=true">Video</a></div></div></div></div>
    <div class="profile-driver__button"><a href="/world-university-rankings/arden-university" class="btn btn-default btn-xs" data-mz="">Explore</a></div>
    </div>              </div>
        </div>
    </div>
    </div>
    <div id="node-623262" class="node node-ranking-institution node-profile_driver member-gold has-logo member-gold clearfix" data-module="profile-driver">
    <div class="profile-driver">
            <div class="profile-driver__banner-image">
            <a href="/world-university-rankings/shenzhen-university" data-mz data-position="driver-image">
            <img class="img-responsive" src="https://www.timeshighereducation.com/sites/default/files/styles/large/public/institution/header_image/header_shenzhen-uni.jpg?itok=H5MWMTXI" alt="" title="" />        </a>
        </div>
            <div class="profile-driver__content">
                <div class="profile-driver__logo">
            <a href="/world-university-rankings/shenzhen-university" data-mz data-position="driver-logo">
                <img class="img-responsive" src="https://www.timeshighereducation.com/sites/default/files/styles/medium/public/shenzhen_university-logo_image.jpg?itok=628kp7Qr" alt="" title="" />          </a>
            </div>
                <div class="profile-driver__links--wrapper">
                    <h3 class="profile-driver__title"><a href="/world-university-rankings/shenzhen-university" data-mz data-position="driver-title">Shenzhen University</a></h3>
                            <div class="profile-driver__ctas"><div class="profile-driver__button"><div class="field field-name-field-institution-video field-type-media field-label-hidden"><div class="field-items"><div class="field-item even"><a class="profile-driver__button-icon btn btn-default btn-xs btn-margin" href="/world-university-rankings/shenzhen-university?popupvideo=true">Video</a></div></div></div></div>
    <div class="profile-driver__button"><a href="/world-university-rankings/shenzhen-university" class="btn btn-default btn-xs" data-mz="">Explore</a></div>
    </div>              </div>
        </div>
    </div>
    </div>
    </div>

    
    </div>
        </div>
        </div>
        </div>
    </div>

    </section>
    </div>

    
    </div>


        <div class="region region-footer-ads">
        <section id="block-the-dfp-the-dfp-footer" class="block block-the-dfp clearfix">

        
    <div id="div-gpt-ad-971806737868556-3" data-ad-page="world-university-rankings" data-ad-unit="21841059662/THE_COM/world-university-rankings/table" data-ad-mobile-size="[320,50]" data-ad-size="[728,90]" data-ad-priority="low" data-ad-position="the_dfp_footer" data-ad-limit="1" class="the-dfp"></div>

    </section>
    </div>

    <footer class="footer" data-module="footer">
        <div class="region region-footer">
        <section id="block-menu-menu-footer-nav" class="block block-menu clearfix">

        
    <ul class="menu nav"><li class="first leaf"><a href="/faqs/general-faqs" title="" data-mz="" data-position="menu">FAQs</a></li>
    <li class="leaf"><a href="/contact-us" title="" data-mz="" data-position="menu">Contact us</a></li>
    <li class="leaf"><a href="/write-times-higher-education" title="" data-mz="" data-position="menu">Write for THE</a></li>
    <li class="leaf"><a href="/terms-and-conditions" title="" data-mz="" data-position="menu">Terms &amp; conditions</a></li>
    <li class="leaf"><a href="/privacy-policy" title="" data-mz="" data-position="menu">Privacy</a></li>
    <li class="leaf"><a href="/cookie-policy" title="" data-mz="" data-position="menu">Cookie policy</a></li>
    <li class="leaf"><a href="/our-partners" title="" data-mz="" data-position="menu">THE Connect</a></li>
    <li class="last leaf"><a href="/media-centre" title="" data-mz="" data-position="menu">Media Centre</a></li>
    </ul>
    </section>
    <section id="block-locale-language" class="block block-locale clearfix">

        
    <ul class="language-switcher-locale-url"><li class="en first active"><a href="/world-university-rankings/2021/world-ranking" class="language-link active" xml:lang="en" hreflang="en" data-mz="" data-position="language-switcher">English</a></li>
    <li class="zh-hans last"><a href="/cn/world-university-rankings/2021/world-ranking" class="language-link" xml:lang="zh-hans" hreflang="zh-hans" data-mz="" data-position="language-switcher">Simplified Chinese (简体中文)</a></li>
    </ul>
    </section>
    <section id="block-the-student-registration-the-student-registration-wall" class="block block-the-student-registration clearfix">

        
    <div class="student-wall-nag js-student-wall-nag">
        <a href="#"
        class="js-student-wall-nag-close student-wall__close-button d-none d-md-block">
            <span class="student-wall__close-button__text">Remind me later </span>
            <span class="student-wall__icon__close"></span></a>
        <div class="student-wall__container">
            <div class="student-wall__wrapper student-wall__row">
                <a href="#"
                class="js-student-wall-nag-close student-wall__close-button d-md-none">
                    <span class="student-wall__icon__close"></span></a>
                <div class="student-wall__description-container student-wall__column">
                    <div class="student-wall__description text-center text-md-left">
                        <div class="student-wall__icon student-wall__icon__publication d-none d-md-block"></div>
                        <div class="student-wall__title the-title">
                            It's completely free to register with THE whether
                            you're a Student or an Higher Education Professional
                        </div>
                        <div class="student-wall__body d-none d-md-block">
                            We know everyone asks you for your details these
                            days. But registering for THE gives you a number of
                            benefits including:
                        </div>
                        <div class="d-none d-md-block">
                            <div class="student-wall__link">
                                <a href="/the-ums-modal/register/nojs" id="modal-register" class="ctools-use-modal  ctools-modal-the-ums-modal-style-xxlarge">Register Now</a>                        </div>
                            <div class="student-wall__existing-user">
                                <span>Already have a THE User ID?</span>  <a href="/the-ums-modal/login/nojs" id="modal-login" class="ctools-use-modal btn--clear ctools-modal-the-ums-modal-style-xlarge">Log in</a>                        </div>
                        </div>
                    </div>
                </div>

                <div class="student-wall__benefits-container student-wall__column">
                    <div class="student-wall__benefits">
                        <div class="student-wall__benefit">
                            <span class="student-wall__icon__bell"></span>
                            <span class="student-wall__benefit-text">Rankings publication alerts</span>
                        </div>
                        <div class="student-wall__benefit">
                            <span class="student-wall__icon__news"></span>
                            <span class="student-wall__benefit-text">Breaking news and latest insights</span>
                        </div>
                        <div class="student-wall__benefit">
                            <span class="student-wall__icon__envelope_alt"></span>
                            <span class="student-wall__benefit-text">Personalised newsletters</span>
                        </div>
                        <div class="student-wall__benefit">
                            <span class="student-wall__icon__calendar_alt"></span>
                            <span class="student-wall__benefit-text">Priority invitations to events</span>
                        </div>
                        <div class="student-wall__benefit">
                            <span class="student-wall__icon__gift"></span>
                            <span class="student-wall__benefit-text">Surveys and prize draws</span>
                        </div>
                        <div class="student-wall__benefit">
                            <span class="student-wall__icon__download_alt"></span>
                            <span class="student-wall__benefit-text">Free downloadable resources</span>
                        </div>
                    </div>
                </div>
                <div class="student-wall__login-container student-wall__column d-md-none text-center">
                    <div class="student-wall__link">
                    <a href="/the-ums-modal/register/nojs" id="modal-register" class="ctools-use-modal  ctools-modal-the-ums-modal-style-xxlarge">Register Now</a>                </div>
                    <div class="student-wall__existing-user">
                        <span>Already have a THE User ID?</span> <a href="/the-ums-modal/login/nojs" id="modal-login" class="ctools-use-modal btn--clear ctools-modal-the-ums-modal-style-xlarge">Log in</a>                    </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    </section>
    </div>

    <section id="footer-top" class="footer-top"><div class="section-container container"><div><div id="the-subscribe" class="the-subscribe footer-top-col"><img class="img-responsive" src="https://www.timeshighereducation.com/sites/default/themes/custom/the_responsive/img/footer/280x280-THE-footer-generic.png" width="221" height="289" alt="Times Higher Education subscriptions" /><p class="footer-section-title">Subscribe</p><p>If you like what you're reading online, why not take advantage of our subscription and get unlimited access to all of <i>Times Higher Education</i>'s content?</p><p>You'll get full access to our website, print and digital editions.</p><a class="btn-the processed" href="/store" data-mz="">Subscribe</a></div></div></div></section>
    </footer>
    <div id="the-nag-footer" class="the-nag-footer the-nag-footer--rankings-advert js-the-nag-footer"><div class="the-nag-footer__content js-the-nag-footer__content"><div id="nag-footer-rankings-ad" data-ad-position="the_dfp_nag_footer" data-ad-limit="1" data-ad-unit="21841059662/THE_COM/world-university-rankings" data-ad-mobile-size="[320,50]" data-ad-size="[728,90]" data-ad-priority="nag" class="the-dfp"></div>
    </div></div>
    <script src="https://www.timeshighereducation.com/sites/default/files/js/js_PdiuypZMI8o81AYEdTHwjRslVPEF69JFzr7Y9sMWt4s.js"></script>
    <script src="https://www.timeshighereducation.com/sites/default/files/js/js_PpH_gB9m1FxGbHH620ZXEBIFrAd-qrH69PxY8yAauco.js"></script>
    <script src="https://www.timeshighereducation.com/sites/default/files/js/js_gVbmYinOZ3jNmhbrFkWWHNSgqARZaX8UVTMRgGksV4w.js"></script>
    <script src="https://www.timeshighereducation.com/sites/default/files/js/js_Hg8MjUq8PnhYOIOZcE20Pthb2glkwOmdTFKDVdn7qow.js"></script>
    <script></script>
    <script src="https://www.timeshighereducation.com/sites/default/files/js/js_tbAkJdzh9LNjiYkJ3TdYlooCUL_byChpIJnfJ_v6Axw.js"></script>
    </body>
    </html>
'''
html = etree.HTML(text)
table = html.xpath('//*[@id="datatable-1"]/thead')[0]
tbody = html.xpath('//*[@id="datatable-1"]/tbody')[0]
row = table.xpath('//*[@id="datatable-1"]/thead/tr//text()')
result = {
    "RANKING": [],
    "SCORES" ：[]
    }

Rank = []
Name_Country_Region = []
No_of_FTE_Students = []
No_of_students_per_staff = []
International_Students = []
Femalew_Male_Ratio = []

print(row)
# print(tbody)
