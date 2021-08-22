from flask import Flask, Response, render_template
import requests
import json
import logging

app = Flask(__name__)



logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def hello_world():
       return "<!DOCTYPE html>
<html lang="es">
<head id="PageHead">
    <!-- Metas -->
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=9,IE=edge,chrome=1" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="keywords" />
    <meta name="description" />

    <meta name="gtm-en-page-url" content="http://www.milestonesys.com/support/tools-and-references/cyber-security/" />
    <meta name="gtm-page-id" content="745749f1-cf43-44c8-9a40-3c22f5c228c2" />
    <meta name="gtm-page-type" content="StandardPage" />
    <meta name="gtm-page-name" content="Cybersecurity" />

    <meta name="facebook-domain-verification" content="uzeicn042frhpdeo6hlynnvogcg0od" />

    <title>Ciberseguridad</title>
    <link rel="canonical" href="http://www.milestonesys.com/es/support/tools-and-references/cyber-security/" />
    <link rel="alternate" hreflang="en" href="http://www.milestonesys.com/support/tools-and-references/cyber-security/" /><link rel="alternate" hreflang="de" href="http://www.milestonesys.com/de/support/tools-and-references/cyber-security/" /><link rel="alternate" hreflang="fr" href="http://www.milestonesys.com/fr/support/tools-and-references/cyber-security/" /><link rel="alternate" hreflang="es" href="http://www.milestonesys.com/es/support/tools-and-references/cyber-security/" /><link rel="alternate" hreflang="it" href="http://www.milestonesys.com/it/support/tools-and-references/cyber-security/" />
            <meta property="og:url" content="https://www.milestonesys.com/es/support/tools-and-references/cyber-security/" />


        <meta property="og:title" content="Ciberseguridad" />






    <link rel="icon" type="image/vnd.microsoft.icon" href="/favicon.ico" />

    <!-- Styles -->
    <link href="/Bundles/Print?v=S-gLPAk2vGq3g-Jehgui869PFTwZrdnq4qpgr5rQRN01" rel="stylesheet" type="text/css" media="print"/>

    <link href='//fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,300,400,700,600' rel='stylesheet' type='text/css' />
    <link href="/Bundles/BaseStyles?v=_qFN6i7zgmyARS7VuhmTzoBrppbCnQLEOzoySzkg0dk1" rel="stylesheet"/>

    <link href="/Bundles/MilestoneStyles?v=YOQWeZUlBDqZRcP9qXWttXijbLlIT_iREp1owG-mc_01" rel="stylesheet"/>


    <link href="/Static/Styles/css/GridTile.min.css" rel="stylesheet" type="text/css" />
<link href="/Static/Plugins/Datatable/buttons.dataTables.min.css" rel="stylesheet" type="text/css" />


    
    


    <script>
        
        window.msysFeatureToggle = (function () {
            var blacklist = ["TFS181353"];
            return {
                blacklist: blacklist,
                isFeatureEnabled: function (id) {
                    return !blacklist.includes(new String(id).toUpperCase());
                }
            }
        })();
    </script>

    <!-- Immedeiate Scripts -->
    <script src="/Static/Scripts/Immediate.js"></script>

<script defer type="text/javascript" src="/Bundles/BaseScripts?v=uG51mEFwmZJ5eZwjtlqEXFCwgsAJ3nm1fBZ3A-i6_1c1"></script>
    <script defer type="text/javascript" src="/Static/Plugins/Datatable/jquery.dataTables.min.js" class="additional"></script>
<script defer type="text/javascript" src="/Static/Plugins/Datatable/dataTables.buttons.min.js" class="additional"></script>
<script defer type="text/javascript" src="/Static/Plugins/Datatable/jszip.min.js" class="additional"></script>
<script defer type="text/javascript" src="/Static/Plugins/Datatable/pdfmake.min.js" class="additional"></script>
<script defer type="text/javascript" src="/Static/Plugins/Datatable/vfs_fonts.min.js" class="additional"></script>
<script defer type="text/javascript" src="/Static/Plugins/Datatable/buttons.html5.min.js" class="additional"></script>
<script defer type="text/javascript" src="/Static/Plugins/Datatable/buttons.print.min.js" class="additional"></script>
<script defer type="text/javascript" src="/Static/Plugins/Datatable/dataTables.input.min.js" class="additional"></script>
<script defer type="text/javascript" src="/Static/Scripts/RunDeferredAdditional.min.js" class="additional"></script>


    <script id="Cookiebot" data-cbid="71f1dae0-4e8b-4339-85e2-b285baec57ce" data-culture="es" data-blockingmode="auto" type="text/javascript"></script>

        <!-- GTM initialization - START -->
        <script type="text/javascript">
            window.dataLayer = window.dataLayer || [];
            function gtag() {
                dataLayer.push(arguments);
            }

            gtag("consent", "default", {
                ad_storage: "denied",
                analytics_storage: "denied",
                wait_for_update: 500
            });
            gtag("set", "ads_data_redaction", true);

            var json = {"getInTouch":"Get in Touch","getInTouchSubmit":"Get in Touch Submit","relatedSolution":"Related Solution - [SOLUTIONNAME]","findSolution":"Find Solutions","print":"Print","tabOverview":"Tab Overview","tabHowItWorks":"Tab How It Works","tabHowToInstall":"Tab How to Install","searchTag":"Search Tag [TAGKEY]","bookADemoToday":"Book a Demo Today","bookADemoTodaySubmit":"Book a Demo Today Submit","downloadDocumentation":"Download - Documentation - [FILETITLE]","readCustomerStory":"Read Customer Story - [FILEURL]","viewCustomerStory":"View Customer Story - [VIDEOURL]","viewAllWithin":"View All Within","recommendThisSolution":"Recommend this Solution","recommendThisSolutionSubmit":"Recommend this Solution Submit","addYourOwnSpecificFeedback":"Add Feedback","addYourOwnSpecificFeedbackSubmit":"Add Feedback Submit","missingInformationSubmit":"Missing information - [MISSINGKEYS]","visitOurWebsite":"Visit our website","followOnLinkedIn":"Follow on LinkedIn","recommendation":"Recommendation - [SOLUTIONNAME]","learnMore":"Learn More - [SOLUTIONNAME]","sendAJoinRequest":"Send a join request","navOverview":"Navigation Overview","navSupport":"Navigation Support","navAdd":"Navigation Add","downloadGuide":"Download - Guide - [FILETITLE]","downloadInstaller":"Download - Installer - [FILETITLE]","ShareFacebook":"ShareFacebook","ShareTwitter":"ShareTwitter","ShareLinkedIn":"ShareLinkedIn","SearchMainTag":"Search Main Tag - [Tag abbreviation]","downloadFreeTrial":"Download - Free trial - [TrialTitle]","seeStatistics":"See statistics","deleteReview":"Delete review","publishReview":"Publish review","toolipfaq":"FAQ - [EnglishFAQName]","tooltipinformation":"Tooltip - Info - [EnglishTooltipName]","tooltipimage":"Tooltip - Image - [EnglishTooltipName]","tooltipvideo":"Tooltip - Video - [EnglishTooltipName]","featurePage":"Feature Page - [URLEnglishPageName]","TagYourContent":"Tag your content - Get in touch","downloadGuideForm":"Download Form - Guide - [FILETITLE]","downloadInstallerForm":"Download Form - Installer - [FILETITLE]","downloadDocumentationForm":"Download Form - Documentation - [FILETITLE]","facetGetInTouch":"Get In Touch Facet - [SOLUTIONID]","facetGetInTouchSubmit":"Get In Touch Facet Submit - [SOLUTIONID]","learnMorePromotedSolution":"Learn More - Promoted Solution - [SOLUTIONID]","subscriptionSelection":"Subscription selection – [SUBSCRIPTIONID] – [SOLUTIONID]","subscriptionDowngrade":"Subscription downgrade – [SUBSCRIPTIONID] – [SOLUTIONID]","subscriptionUpgrade":"Subscription upgrade – [SUBSCRIPTIONID] – [SOLUTIONID]","subscriptionCancellation":"Subscription cancellation – [SUBSCRIPTIONID] – [SOLUTIONID]","solutionModelReadMore":"Solution model read more - [Unique challenge key from taxonomy]","tabCertifications":"Tab Certifications","tabAwards":"Tab Awards","tabDownloads":"Tab Downloads","tabOurProductExperience":"Our Product Experience Tab","goToProductPage":"Go To Product page - [SOLUTIONID]","tabMilestoneSoftware":"Milestone Software Tab","tabReviews":"Reviews Tab","solutionModelChallenges":"Solution model challenge - [Unique challenge key from taxonomy]","howWeSupportYou":"How we support you - [Unique support key from taxonomy]","exploreChallenge":"Explore challenge - [Unique challenge key from taxonomy]","tabEditPages":"Edit Pages Tab - [SolutionName]","tabUserReviews":"User Reviews Tab - [SolutionName]","tabPageFeedback":"Page Feedback Tab - [SolutionName]","tabAnalytics":"Analytics Tab - [SolutionName]","downloadFormSubmit":"Download Form Submit","tabCompany":"Tab Company","ShareEmail":"ShareEmail","learnMorePromotedExpertise":"Learn More - Promoted Expertise - [SOLUTIONID]"};
            window['__msgtm'] = json;
        </script>
        <!--Send User Id when the user logs in the first time -->
        <script type="text/javascript">
            (function (w, d, s, l, i) {
                w[l] = w[l] || []; w[l].push({
                    'gtm.start':
                        new Date().getTime(), event: 'gtm.js'
                }); var f = d.getElementsByTagName(s)[0],
                    j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : ''; j.async = true; j.src =
                    'https://www.googletagmanager.com/gtm.js?id=' + i + dl; f.parentNode.insertBefore(j, f);
            })(window, document, 'script', 'dataLayer', 'GTM-WBN9RS');
        </script>
    <!-- GTM initialization - END -->

    <noscript>
        <style>
            .js-required {
                display: none;
            }
        </style>
    </noscript>
<link href="/Static/dist/legacyRoot~rootBasic.75578bace29355ad1f6d.css" rel="stylesheet"><link href="/Static/dist/legacyRoot.3c57931f9e1f5eeb95f2.css" rel="stylesheet"><link href="/Static/dist/marketplaceBundle.c5334710a8d0532fbb6b.css" rel="stylesheet"><script defer src="/Static/dist/runtime.48d5717fe03ed596e329.js"></script><script defer src="/Static/dist/2.f615c8c88487eb03bb67.js"></script><script defer src="/Static/dist/legacyRoot~rootBasic.f293fe8d1d767907ff19.js"></script><script defer src="/Static/dist/legacyRoot.c5fb13874b20db4cd278.js"></script><script defer src="/Static/dist/marketplaceBundle.d729aa0b40db13053f39.js"></script></head>
<body class="responsive">
    <noscript>
            <!-- End Google Tag Manager (noscript) -->
            <iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WBN9RS"
                    height="0" width="0" style="display:none;visibility:hidden"></iframe>
            <!-- Google Tag Manager (noscript) -->
        <div class="no-script noprint">
            La funci&#243;n que desea acceder depende de JavaScript, que no est&#225; habilitado en su navegador. Habilite JavaScript y vuelva a intentarlo.
        </div>
    </noscript>

    
    

    



<div id="HeaderSection" class="container-fluid">
    
    

    
	<div class="row"><div class="header col-12 col-xs-12 col-12">


<div class="header-container desktop">

    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="links">
        <div class="milestone-logo">
            <a href="/es" class="headerlogolink"></a>
        </div>
        <button class="burger-menu-link" type="button" data-target="#MainMenu">
            <div class="ms-icon">
                <svg>
                    <use xlink:href="/Static/Img/Icons/icons.svg#burger-icon"></use>
                </svg>
            </div>
        </button>
        <button class="account-menu-link" type="button">
            <div class="ms-icon">
                <svg>
                    <use xlink:href="/Static/Img/Icons/icons.svg#profile"></use>
                </svg>
            </div>
        </button>
            <button class="language-menu-link" type="button">
                <div class="ms-icon">
                    <svg>
                        <use xlink:href="/Static/Img/Icons/icons.svg#globe"></use>
                    </svg>
                </div>
            </button>

        <div class="menu-button-with-dropdown menu-button-with-dropdown--signin-menu show-desktop"><input class="menu-button-with-dropdown__checkbox" id="state-signin-menu" type="checkbox"></input>
<label class="menu-button-with-dropdown__button" for="state-signin-menu"><span class="menu-button-with-dropdown__button-text">Inicio de sesi&#243;n</span>

<svg class="menu-button-with-dropdown__button-icon"><use xlink:href="/Static/Img/Icons/icons.svg#profile"></use></svg>
</label>
<ul class="menu-button-with-dropdown__menu"><li class="menu-button-with-dropdown__menu-item"><a class="menu-button-with-dropdown__menu-item-link" href="/my-milestone/">My Milestone</a></li>
<li class="menu-button-with-dropdown__menu-item"><a class="menu-button-with-dropdown__menu-item-link" href="/es/my-milestone/marketplace/">Marketplace</a></li>
</ul></div><div class="signin-menu-mobil show-mobile"><div class="navigation-overlay"><ul class="nav"><li><a href="/my-milestone/">My Milestone</a></li>
<li><a href="/es/my-milestone/marketplace/">Marketplace</a></li>
</ul></div>
</div>

<form action="/HeaderBlock/Logout" method="post"><input name="__RequestVerificationToken" type="hidden" value="3t9xhrBJ4qArb5SdXmFdh4yzOyr3sHiUuezrIUlprHYv5T9Zn4IiLOqPEobaH3iBxRD66akBZIuSiAfkbKAHxOrGukY1" />            <button id="logout-button" type="submit"></button>
</form>
            <div class="menu-button-with-dropdown menu-button-with-dropdown--language-menu show-desktop">
        <input class="menu-button-with-dropdown__checkbox" id="state-language-menu" type="checkbox">
        <label class="menu-button-with-dropdown__button" for="state-language-menu">
            <svg class="menu-button-with-dropdown__button-icon">
                <use xlink:href="/Static/Img/Icons/icons.svg#globe"></use>
            </svg>
            <span class="menu-button-with-dropdown__button-text">espa&#241;ol</span>
        </label>
        <ul class="menu-button-with-dropdown__menu">
            <li class="menu-button-with-dropdown__menu-title">SITIO WEB COMPLETO TRADUCIDO</li>
                <li class="menu-button-with-dropdown__menu-item">
                    <a class="menu-button-with-dropdown__menu-item-link "
                       href="https://www.milestonesys.com/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">
                        English
                    </a>
                </li>
                <li class="menu-button-with-dropdown__menu-item">
                    <a class="menu-button-with-dropdown__menu-item-link "
                       href="https://www.milestonesys.com/fr/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">
                        fran&#231;ais
                    </a>
                </li>
                <li class="menu-button-with-dropdown__menu-item">
                    <a class="menu-button-with-dropdown__menu-item-link menu-button-with-dropdown__menu-item-link--active"
                       href="https://www.milestonesys.com/es/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">
                        espa&#241;ol
                    </a>
                </li>
                <li class="menu-button-with-dropdown__menu-item">
                    <a class="menu-button-with-dropdown__menu-item-link "
                       href="https://www.milestonesys.com/it/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">
                        italiano
                    </a>
                </li>
                <li class="menu-button-with-dropdown__menu-item">
                    <a class="menu-button-with-dropdown__menu-item-link "
                       href="https://www.milestonesys.com/de/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">
                        Deutsch
                    </a>
                </li>
            <li class="menu-button-with-dropdown__menu-separator"></li>
            <li class="menu-button-with-dropdown__menu-title">P&#193;GINAS M&#193;S POPULARES TRADUCIDAS</li>
                <li class="menu-button-with-dropdown__menu-item">
                    <a class="menu-button-with-dropdown__menu-item-link "
                       href="https://www.milestonesys.com/ru/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">
                        русский
                    </a>
                </li>
                <li class="menu-button-with-dropdown__menu-item">
                    <a class="menu-button-with-dropdown__menu-item-link "
                       href="https://www.milestonesys.com/sv/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">
                        svenska
                    </a>
                </li>
                <li class="menu-button-with-dropdown__menu-item">
                    <a class="menu-button-with-dropdown__menu-item-link "
                       href="https://www.milestonesys.com/no/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">
                        norsk
                    </a>
                </li>
                <li class="menu-button-with-dropdown__menu-item">
                    <a class="menu-button-with-dropdown__menu-item-link "
                       href="https://www.milestonesys.com/da/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">
                        dansk
                    </a>
                </li>
                <li class="menu-button-with-dropdown__menu-item">
                    <a class="menu-button-with-dropdown__menu-item-link "
                       href="https://www.milestonesys.com/fi/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">
                        suomi
                    </a>
                </li>
                <li class="menu-button-with-dropdown__menu-item">
                    <a class="menu-button-with-dropdown__menu-item-link "
                       href="https://www.milestonesys.com/nl/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">
                        Nederlands
                    </a>
                </li>
                <li class="menu-button-with-dropdown__menu-item">
                    <a class="menu-button-with-dropdown__menu-item-link "
                       href="https://www.milestonesys.com/ja/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">
                        日本語
                    </a>
                </li>
                <li class="menu-button-with-dropdown__menu-item">
                    <a class="menu-button-with-dropdown__menu-item-link "
                       href="https://www.milestonesys.com/tr/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">
                        T&#252;rk&#231;e
                    </a>
                </li>
        </ul>
    </div>

            <div class="language-menu-mobile show-mobile">
        <div class="navigation-overlay">
            <ul class=" language-navigation primary-langauges  nav">
                <li class="language-navigation__headline">
                    SITIO WEB COMPLETO TRADUCIDO
                </li>
                    <li>
                        <div class="language-navigation__container ">
                            <a class="language-navigation__language-link" href="https://www.milestonesys.com/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">English</a>

                            <div class="language-navigation__icon-wrapper ms-icon">
                                <svg class="language-navigation__icon">
                                    <use xlink:href="/Static/Img/Icons/icons.svg#globe"></use>
                                </svg>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="language-navigation__container ">
                            <a class="language-navigation__language-link" href="https://www.milestonesys.com/fr/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">fran&#231;ais</a>

                            <div class="language-navigation__icon-wrapper ms-icon">
                                <svg class="language-navigation__icon">
                                    <use xlink:href="/Static/Img/Icons/icons.svg#globe"></use>
                                </svg>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="language-navigation__container active">
                            <a class="language-navigation__language-link" href="https://www.milestonesys.com/es/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">espa&#241;ol</a>

                            <div class="language-navigation__icon-wrapper ms-icon">
                                <svg class="language-navigation__icon">
                                    <use xlink:href="/Static/Img/Icons/icons.svg#globe"></use>
                                </svg>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="language-navigation__container ">
                            <a class="language-navigation__language-link" href="https://www.milestonesys.com/it/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">italiano</a>

                            <div class="language-navigation__icon-wrapper ms-icon">
                                <svg class="language-navigation__icon">
                                    <use xlink:href="/Static/Img/Icons/icons.svg#globe"></use>
                                </svg>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="language-navigation__container ">
                            <a class="language-navigation__language-link" href="https://www.milestonesys.com/de/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">Deutsch</a>

                            <div class="language-navigation__icon-wrapper ms-icon">
                                <svg class="language-navigation__icon">
                                    <use xlink:href="/Static/Img/Icons/icons.svg#globe"></use>
                                </svg>
                            </div>
                        </div>
                    </li>
            </ul>
            <ul class="nav language-navigation secondary-langauges">

                <li class="language-navigation__headline">
                    P&#193;GINAS M&#193;S POPULARES TRADUCIDAS
                </li>
                    <li>
                        <div class="language-navigation__container ">
                            <a class="language-navigation__language-link" href="https://www.milestonesys.com/ru/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">русский </a>

                            <div class="language-navigation__icon-wrapper ms-icon">
                                <svg class="language-navigation__icon">
                                    <use xlink:href="/Static/Img/Icons/icons.svg#globe"></use>
                                </svg>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="language-navigation__container ">
                            <a class="language-navigation__language-link" href="https://www.milestonesys.com/sv/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">svenska </a>

                            <div class="language-navigation__icon-wrapper ms-icon">
                                <svg class="language-navigation__icon">
                                    <use xlink:href="/Static/Img/Icons/icons.svg#globe"></use>
                                </svg>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="language-navigation__container ">
                            <a class="language-navigation__language-link" href="https://www.milestonesys.com/no/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">norsk </a>

                            <div class="language-navigation__icon-wrapper ms-icon">
                                <svg class="language-navigation__icon">
                                    <use xlink:href="/Static/Img/Icons/icons.svg#globe"></use>
                                </svg>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="language-navigation__container ">
                            <a class="language-navigation__language-link" href="https://www.milestonesys.com/da/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">dansk </a>

                            <div class="language-navigation__icon-wrapper ms-icon">
                                <svg class="language-navigation__icon">
                                    <use xlink:href="/Static/Img/Icons/icons.svg#globe"></use>
                                </svg>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="language-navigation__container ">
                            <a class="language-navigation__language-link" href="https://www.milestonesys.com/fi/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">suomi </a>

                            <div class="language-navigation__icon-wrapper ms-icon">
                                <svg class="language-navigation__icon">
                                    <use xlink:href="/Static/Img/Icons/icons.svg#globe"></use>
                                </svg>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="language-navigation__container ">
                            <a class="language-navigation__language-link" href="https://www.milestonesys.com/nl/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">Nederlands </a>

                            <div class="language-navigation__icon-wrapper ms-icon">
                                <svg class="language-navigation__icon">
                                    <use xlink:href="/Static/Img/Icons/icons.svg#globe"></use>
                                </svg>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="language-navigation__container ">
                            <a class="language-navigation__language-link" href="https://www.milestonesys.com/ja/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">日本語 </a>

                            <div class="language-navigation__icon-wrapper ms-icon">
                                <svg class="language-navigation__icon">
                                    <use xlink:href="/Static/Img/Icons/icons.svg#globe"></use>
                                </svg>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="language-navigation__container ">
                            <a class="language-navigation__language-link" href="https://www.milestonesys.com/tr/support/tools-and-references/cyber-security/?gclid=CjwKCAjw64eJBhAGEiwABr9o2Mq0qzp-Rd0ulF841cl04OP656jYR8MR9ktulJQXxMMjXEyIa8TNJBoC0R8QAvD_BwE">T&#252;rk&#231;e </a>

                            <div class="language-navigation__icon-wrapper ms-icon">
                                <svg class="language-navigation__icon">
                                    <use xlink:href="/Static/Img/Icons/icons.svg#globe"></use>
                                </svg>
                            </div>
                        </div>
                    </li>

                
                <li class="additional-tab"></li>
            </ul>
        </div>
    </div>

        
<div class="searchcontrol">
    <form id="SearchFormId" method="post">
        <input id="SearchEvent" name="SearchEvent" type="hidden" value="/es/HeaderBlock/DoSearch" />


            <div class="search-button">
                <div class="ms-icon">
                    <svg>
                        <use xlink:href="/Static/Img/Icons/icons.svg#search-icon"></use>
                    </svg>
                </div>
                <span class="icon"></span>
            </div>
        <span class="separator">|</span>
        <div class="overlay">
            <div class="search-submit ms-icon">
                <svg>
                    <use xlink:href="/Static/Img/Icons/icons.svg#search-icon"></use>
                </svg>
            </div>
            <input type="text" name="txtGlobalSearch" id="txtGlobalSearch" placeholder="Buscar aqu&#237;" />
            <input type="hidden" name="globalSearchResultsUrl" value="/es/search-results/">
        </div>
    </form>
</div>
        <div class="show-desktop hidefirst header-links"><a href="/es/comunidad/encuentre-un-socio-de-milestone/">D&#243;nde comprarlo</a>
<span>|</span>
<a href="/es/about-us/">Acerca de nosotros</a>
<span>|</span>
<a href="/es/about-us/career/">Carreras profesionales</a>
<span>|</span>
</div>
    </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="navigation">
            <nav id="MainMenu" class="navigation-overlay slide-right">
                <ul class="nav navbar-nav menuitems">
                        <li>
                            <a href="/es/solutions/">Soluciones</a><div class="open-icon"><div class="divider"></div><div class="image"></div></div>

<ul class="menuitems"><li><a class="non-clickable" href="/es/solutions/plataforma/" onclick="return false;" style="padding-left:18px">Plataforma</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/solutions/plataforma/por-que-escoger-milestone/" style="padding-left:36px">&#191;Por qu&#233; escoger Milestone?</a>
</li>
<li><a href="/es/solutions/plataforma/video-management-software/" style="padding-left:36px">Software de gesti&#243;n de v&#237;deo</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/solutions/plataforma/video-management-software/xprotect-essential/" style="padding-left:54px">XProtect Essential+</a>
</li>
<li><a href="/es/solutions/plataforma/video-management-software/xprotect-express/" style="padding-left:54px">XProtect Express+</a>
</li>
<li><a href="/es/solutions/plataforma/video-management-software/xprotect-professional/" style="padding-left:54px">XProtect Professional+</a>
</li>
<li><a href="/es/solutions/plataforma/video-management-software/xprotect-expert/" style="padding-left:54px">XProtect Expert</a>
</li>
<li><a href="/es/solutions/plataforma/video-management-software/xprotect-corporate/" style="padding-left:54px">XProtect Corporate</a>
</li>
</ul>
</li>
<li><a href="/es/solutions/plataforma/XProtect-Clients/" style="padding-left:36px">Clientes XProtect</a>
</li>
<li><a href="/es/solutions/plataforma/xprotect-cloud-solutions/" style="padding-left:36px">XProtect Cloud Solutions</a>
</li>
<li><a href="/es/solutions/plataforma/indice-de-productos/" style="padding-left:36px">&#205;ndice de productos</a>
</li>
<li><a href="/es/solutions/plataforma/try-our-software/" style="padding-left:36px">Pruebe nuestro software</a>
</li>
<li><a class="googlelinktracking" data-category="DemoCampaign_es" data-enable-google-event-tracking="True" data-label="Navigation_BookAFreeVMSDemo_es" href="/es/campaigns/book-a-demo/" style="padding-left:36px">Reserva una demostraci&#243;n VMS gratuita</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/solutions/hardware-y-add-on/" onclick="return false;" style="padding-left:18px">Hardware y Add-on</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/solutions/hardware-y-add-on/why-choose-Husky/" style="padding-left:36px">&#191;Por qu&#233; elegir Husky IVO?</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="HuskyIVOSeries" data-enable-google-event-tracking="True" data-label="Navigation_CustomLink_ExploreHuskyIVO" href="/es/solutions/hardware-y-add-on/HuskyIVO-series/" style="padding-left:54px" target="_self">Explore the Husky IVO Series</a>
</li>
<li><a class="googlelinktracking" data-category="HuskyIVOSeries" data-enable-google-event-tracking="True" data-label="Navigation_CustomLink_HuskyXSeries" href="/es/solutions/hardware-y-add-on/network-video-recorders/" style="padding-left:54px" target="_self">X Series</a>
</li>
</ul>
</li>
<li><a href="/es/solutions/hardware-y-add-on/HuskyIVO-series/" style="padding-left:36px">Dispositivos de v&#237;deo Husky IVO</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/solutions/hardware-y-add-on/HuskyIVO-series/Husky-IVO-150D/" style="padding-left:54px">Husky IVO 150D</a>
</li>
<li><a href="/es/solutions/hardware-y-add-on/HuskyIVO-series/Husky-IVO-350T/" style="padding-left:54px">Husky IVO 350T</a>
</li>
<li><a href="/es/solutions/hardware-y-add-on/HuskyIVO-series/Husky-IVO-350R/" style="padding-left:54px">Husky IVO 350R</a>
</li>
<li><a href="/es/solutions/hardware-y-add-on/HuskyIVO-series/Husky-IVO-700R/" style="padding-left:54px">Husky IVO 700R</a>
</li>
<li><a href="/es/solutions/hardware-y-add-on/HuskyIVO-series/Husky-IVO-1000R/" style="padding-left:54px">Husky IVO 1000R</a>
</li>
<li><a href="/es/solutions/hardware-y-add-on/HuskyIVO-series/Husky-IVO-1800R/" style="padding-left:54px">Husky IVO 1800R</a>
</li>
</ul>
</li>
<li><a href="/es/solutions/hardware-y-add-on/productos-add-on-de-milestone/" style="padding-left:36px">Productos add-on de Milestone</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/solutions/hardware-y-add-on/productos-add-on-de-milestone/access/" style="padding-left:54px">Acceso</a>
</li>
<li><a href="/es/solutions/hardware-y-add-on/productos-add-on-de-milestone/lpr/" style="padding-left:54px">LPR</a>
</li>
<li><a href="/es/solutions/hardware-y-add-on/productos-add-on-de-milestone/transact/" style="padding-left:54px">Transact</a>
</li>
<li><a href="/es/solutions/hardware-y-add-on/productos-add-on-de-milestone/retail/" style="padding-left:54px">Retail</a>
</li>
<li><a href="/es/solutions/hardware-y-add-on/productos-add-on-de-milestone/smart-wall/" style="padding-left:54px">Smart Wall</a>
</li>
<li><a href="/es/solutions/hardware-y-add-on/productos-add-on-de-milestone/screen-recorder/" style="padding-left:54px">Screen Recorder</a>
</li>
<li><a href="/es/solutions/hardware-y-add-on/productos-add-on-de-milestone/interconnect/" style="padding-left:54px">Interconnect</a>
</li>
</ul>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="SupportedDevices_HardwareAndAddOns_es" href="/es/comunidad/herramientas-de-socios-comerciales/supported-devices/" style="padding-left:36px">Dispositivos compatibles</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/solutions/services/" onclick="return false;" style="padding-left:18px">Servicios</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="ServiceOverview_es" href="/es/solutions/services/" style="padding-left:36px">Visi&#243;n general de servicios</a>
</li>
<li><a href="/es/solutions/services/milestone-care/" style="padding-left:36px">Milestone Care™</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/solutions/services/milestone-care/care-plus/" style="padding-left:54px">Care Plus</a>
</li>
<li><a href="/es/solutions/services/milestone-care/care-premium/" style="padding-left:54px">Care Premium</a>
</li>
</ul>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Milestone_Learning" href="https://learn.milestonesys.com/index.htm" style="padding-left:36px">Milestone Learning</a>
</li>
<li><a href="/es/solutions/services/customer-dashboard/" style="padding-left:36px">Panel del Cliente</a>
</li>
<li><a href="/es/solutions/services/servicios-profesionales/" style="padding-left:36px">Servicios Profesionales</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="CustomDevelopment_es" href="/es/comunidad/herramientas-de-desarrolladores/custom-development/" style="padding-left:36px">Custom Development</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="Nav_Services_VersionComparisonTool_es" href="/es/comunidad/herramientas-de-socios-comerciales/xprotect-comparison-tools/" style="padding-left:36px">Herramienta de comparaci&#243;n de versiones</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/solutions/industrias/" onclick="return false;" style="padding-left:18px">Industrias</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/solutions/industrias/education/" style="padding-left:36px">Education</a>
</li>
<li><a href="/es/solutions/industrias/public-transportation/" style="padding-left:36px">Public Transportation</a>
</li>
<li><a href="/es/solutions/industrias/retail/" style="padding-left:36px">Retail</a>
</li>
<li><a href="/es/solutions/industrias/safe-cities/" style="padding-left:36px">Safe cities</a>
</li>
<li><a href="/es/solutions/industrias/transportation/" style="padding-left:36px">Transportation</a>
</li>
<li><a href="/es/solutions/industrias/us-federal-government/" style="padding-left:36px">US Federal Government</a>
</li>
</ul>
</li>
</ul>                        </li>
                        <li>
                            <a href="/es/comunidad/">Comunidad</a><div class="open-icon"><div class="divider"></div><div class="image"></div></div>

<ul class="menuitems"><li><a class="non-clickable" href="/es/comunidad/hagase-socio/" onclick="return false;" style="padding-left:18px">H&#225;gase socio</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/comunidad/hagase-socio/la-plataforma-abierta/" style="padding-left:36px">La plataforma abierta</a>
</li>
<li><a href="/es/comunidad/hagase-socio/distributor/" style="padding-left:36px">Distribuidor</a>
</li>
<li><a href="/es/comunidad/hagase-socio/technology-partner-program/" style="padding-left:36px">Technology Partner Program</a>
</li>
<li><a href="/es/comunidad/hagase-socio/reseller/" style="padding-left:36px">Revendedor</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/comunidad/herramientas-de-desarrolladores/" onclick="return false;" style="padding-left:18px">Herramientas de desarrolladores</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="DownloadSoftware_DeveloperTools_es" href="/es/support/resources/download-software/" style="padding-left:36px">Descargar software</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="new_DeveloperForum_DeveloperTools_es" href="http://developer.milestonesys.com/" style="padding-left:36px" target="_blank">Foro para desarrolladores</a>
</li>
<li><a href="/es/comunidad/herramientas-de-desarrolladores/milestone-developer-champions/" style="padding-left:36px">Milestone Developer Champions</a>
</li>
<li><a href="/es/comunidad/herramientas-de-desarrolladores/kickstarter-contest-2021/" style="padding-left:36px">Kickstarter Contest</a>
</li>
<li><a href="/es/comunidad/herramientas-de-desarrolladores/sdk/" style="padding-left:36px">SDK</a>
</li>
<li><a href="/es/comunidad/herramientas-de-desarrolladores/custom-development/" style="padding-left:36px">Custom Development</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="FindProductMaterials_DeveloperTools_es" href="https://content.milestonesys.com/" style="padding-left:36px" target="_blank">Portal de contenidos</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="MyMilestone_DeveloperTools_es" href="/es/my-milestone/" style="padding-left:36px">My Milestone</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Cybersecurity_DeveloperTools" href="/es/support/tools-and-references/cyber-security/" style="padding-left:36px">Cybersecurity</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/comunidad/herramientas-de-socios-comerciales/" onclick="return false;" style="padding-left:18px">Herramientas de socios comerciales</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/comunidad/herramientas-de-socios-comerciales/supported-devices/" style="padding-left:36px">Dispositivos compatibles</a>
</li>
<li><a href="/es/comunidad/herramientas-de-socios-comerciales/device-packs/" style="padding-left:36px">Device Packs</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="DownloadSoftware_BusinessPartnerTools_es" href="/es/support/resources/download-software/" style="padding-left:36px">Descargar software</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="FindProductMaterials_BusinessPartnerTools_es" href="https://content.milestonesys.com/" style="padding-left:36px" target="_blank">Portal de contenidos</a>
</li>
<li><a href="/es/comunidad/herramientas-de-socios-comerciales/xprotect-comparison-tools/" style="padding-left:36px">XProtect Comparison Tools</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="CustomerDashboard_es" href="/es/solutions/services/customer-dashboard/" style="padding-left:36px">Customer Dashboard</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="ServerCalculator_BusinessPartnerTools_es" href="/es/my-milestone/default/xprotect-server-calculator/" style="padding-left:36px">Calculador de servidores</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="DocumentationPortal_Community_BPT" href="https://doc.milestonesys.com/?utm_source=MSweb&amp;utm_medium=Megamenu&amp;utm_campaign=Permanent" style="padding-left:36px" target="_self">Milestone Documentation</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="LearningAndPerformance_BusinessPartnerTools_es" href="https://learn.milestonesys.com/index.htm" style="padding-left:36px">Formaci&#243;n y rendimiento</a>
</li>
<li><a href="/es/comunidad/herramientas-de-socios-comerciales/global-bid-desk/" style="padding-left:36px">Global Bid Desk</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="MyMilestone_BusinessPartnerTools_es" href="/es/my-milestone/" style="padding-left:36px">My Milestone</a>
</li>
<li><a href="/es/comunidad/herramientas-de-socios-comerciales/architects-and-engineers/" style="padding-left:36px">Arquitectos e ingenieros</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/comunidad/marketplace/" onclick="return false;" style="padding-left:18px">Marketplace</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/comunidad/marketplace/start-exploring/" style="padding-left:36px">Empiece a descubrir</a>
</li>
<li><a href="/es/comunidad/marketplace/what-is-marketplace/" style="padding-left:36px">&#191;Qu&#233; es Milestone Marketplace?</a>
</li>
<li><a href="/es/comunidad/marketplace/join-marketplace/" style="padding-left:36px">Join Marketplace</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="Nav_Marketplace_login_es" href="/my-milestone/marketplace/" style="padding-left:36px" target="_blank">Iniciar sesi&#243;n en Marketplace</a>
</li>
<li><a href="/es/comunidad/marketplace/support/" style="padding-left:36px">Marketplace Support</a>
</li>
</ul>
</li>
</ul>                        </li>
                        <li>
                            <a data-category="Marketplace_Main_Nav" data-label="MP_Start_Exploring_First_Level" data-enable-google-event-tracking="True" href="/es/comunidad/marketplace/start-exploring/" target="_self" class="googlelinktracking">Marketplace</a><div class="open-icon"><div class="divider"></div><div class="image"></div></div>

<ul class="menuitems"><li><a class="non-clickable" href="/es/milestone-marketplace/milestone-marketplace/" onclick="return false;" style="padding-left:18px">Milestone Marketplace</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="Marketplace_Main_Nav_es" data-enable-google-event-tracking="True" data-label="MP_Start_Exploring_Second_Level_es" href="/es/comunidad/marketplace/start-exploring/" style="padding-left:36px" target="_self">Empiece a descubrir</a>
</li>
<li><a class="googlelinktracking" data-category="Marketplace_Main_Nav_es" data-enable-google-event-tracking="True" data-label="MP_What_is_MP_es" href="/es/under-construction/lavinia/what-is-marketplace/" style="padding-left:36px" target="_self">&#191;En qu&#233; consiste Marketplace?</a>
</li>
<li><a class="googlelinktracking" data-category="Marketplace_Main_Nav_es" data-enable-google-event-tracking="True" data-label="MP_Join_Milestone_es" href="/es/under-construction/lavinia/join-marketplace/" style="padding-left:36px" target="_self">&#218;nase a Marketplace</a>
</li>
<li><a class="googlelinktracking" data-category="Marketplace_Main_Nav_es" data-enable-google-event-tracking="True" data-label="MP_Marketplace Login_es" href="/es/my-milestone/marketplace/" style="padding-left:36px" target="_self">Iniciar sesi&#243;n en Marketplace</a>
</li>
<li><a class="googlelinktracking" data-category="Marketplace_Main_Nav_es" data-enable-google-event-tracking="True" data-label="MP_Marketplace_Support_es" href="/es/comunidad/marketplace/support/" style="padding-left:36px" target="_self">Asistencia de Marketplace</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/milestone-marketplace/challenges/" onclick="return false;" style="padding-left:18px">Challenges</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/milestone-marketplace/challenges/understand-customer-behavior/" style="padding-left:36px">Understand customer behavior</a>
</li>
<li><a href="/es/milestone-marketplace/challenges/prevent-vandalism/" style="padding-left:36px">Prevent Vandalism</a>
</li>
<li><a href="/es/milestone-marketplace/challenges/gather-evidence/" style="padding-left:36px">Gather evidence for criminal investigations</a>
</li>
<li><a href="/es/milestone-marketplace/challenges/respond-to-medical-emergencies/" style="padding-left:36px">Respond to medical emergencies</a>
</li>
<li><a href="/es/milestone-marketplace/challenges/control-access-to-restricted-areas/" style="padding-left:36px">Control access to restricted areas</a>
</li>
<li><a href="/es/milestone-marketplace/challenges/provide-situational-awareness/" style="padding-left:36px">Provide situational awareness</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/milestone-marketplace/areas-of-practice/" onclick="return false;" style="padding-left:18px">Areas of practice</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/milestone-marketplace/areas-of-practice/central-monitoring/" style="padding-left:36px">Central Monitoring</a>
</li>
<li><a href="/es/milestone-marketplace/areas-of-practice/surveillance/" style="padding-left:36px">Surveillance</a>
</li>
<li><a href="/es/milestone-marketplace/areas-of-practice/access-control/" style="padding-left:36px">Access Control</a>
</li>
<li><a href="/es/milestone-marketplace/areas-of-practice/investigation/" style="padding-left:36px">Investigation</a>
</li>
<li><a href="/es/milestone-marketplace/areas-of-practice/tracking-monitoring/" style="padding-left:36px">Tracking &amp; Monitoring</a>
</li>
<li><a href="/es/milestone-marketplace/areas-of-practice/detection/" style="padding-left:36px">Detection</a>
</li>
<li><a href="/es/milestone-marketplace/areas-of-practice/intrusion-alarm/" style="padding-left:36px">Intrusion &amp; Alarm</a>
</li>
<li><a href="/es/milestone-marketplace/areas-of-practice/vehicles-traffic/" style="padding-left:36px">Vehicles &amp; Traffic</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/milestone-marketplace/technologies/" onclick="return false;" style="padding-left:18px">Technologies</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/milestone-marketplace/technologies/facial-recognition/" style="padding-left:36px">Facial Recognition</a>
</li>
<li><a href="/es/milestone-marketplace/technologies/voice-recognition/" style="padding-left:36px">Voice Recognition</a>
</li>
<li><a href="/es/milestone-marketplace/technologies/smoke-detection/" style="padding-left:36px">Smoke Detection</a>
</li>
<li><a href="/es/milestone-marketplace/technologies/motion-detection/" style="padding-left:36px">Motion Detection</a>
</li>
<li><a href="/es/milestone-marketplace/technologies/GPS-tracking/" style="padding-left:36px">GPS Tracking</a>
</li>
<li><a href="/es/milestone-marketplace/technologies/access-control/" style="padding-left:36px">Access Control</a>
</li>
<li><a href="/es/milestone-marketplace/technologies/GIS/" style="padding-left:36px">GIS</a>
</li>
<li><a href="/es/milestone-marketplace/technologies/ANPR/" style="padding-left:36px">ANPR</a>
</li>
<li><a href="/es/milestone-marketplace/technologies/body-worn-solutions/" style="padding-left:36px">Body-Worn Solutions</a>
</li>
</ul>
</li>
</ul>                        </li>
                        <li>
                            <a href="/es/support/" class="active">Asistencia</a><div class="open-icon"><div class="divider"></div><div class="image"></div></div>

<ul class="menuitems"><li><a class="non-clickable" href="/es/support/self-service-and-support/" onclick="return false;" style="padding-left:18px">Self-Service &amp; Support</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="KnowledgeBase_es" href="https://supportcommunity.milestonesys.com/s/knowledgebase" style="padding-left:36px" target="_blank">Base de conocimientos</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="SupportCommunity_es" href="https://supportcommunity.milestonesys.com/s/" style="padding-left:36px" target="_blank">Comunidad de Asistencia</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="new_DeveloperForum_HelpYourself_es" href="http://developer.milestonesys.com/" style="padding-left:36px" target="_blank">Foro para desarrolladores</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="eLearning_es" href="https://learn.milestonesys.com/index.htm" style="padding-left:36px">Portal de formaci&#243;n</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Nav_HelpYourself_ DeploymentAssistant" href="https://www.milestonesys.com/deployment-assistant" style="padding-left:36px" target="_blank">Milestone Deployment Assistant</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Nav_SelfServiceandSupport_ DocumentationPortal" href="https://doc.milestonesys.com/?utm_source=MSweb&amp;utm_medium=Megamenu&amp;utm_campaign=Permanent" style="padding-left:36px" target="_self">Milestone Documentation</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="WhitePapers_es" href="https://content.milestonesys.com/search/set/?resetsearch&amp;field=metaproperty_Assettype&amp;value=Whitepaper&amp;multiple=false&amp;filterType=add&amp;filterkey=savedFilters" style="padding-left:36px" target="_blank">Documentos t&#233;cnicos</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_Support" data-enable-google-event-tracking="True" data-label="ContentPortal" href="https://content.milestonesys.com/" style="padding-left:36px">Content Portal</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_Support" data-enable-google-event-tracking="True" data-label="SupportWebinars_es" href="/es/events/" style="padding-left:36px">Seminarios web de asistencia</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="XProtectEssentialSupport_es" href="/es/solutions/plataforma/video-management-software/xprotect-essential/ayuda-de-essential2/" style="padding-left:36px">Asistencia de XProtect Essential+</a>
</li>
<li><a href="/es/support/self-service-and-support/husky-support/" style="padding-left:36px">Asistencia Husky serie X</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/support/self-service-and-support/husky-support/HuskyX2-support/" style="padding-left:54px">Asistencia de Husky X2</a>
</li>
<li><a href="/es/support/self-service-and-support/husky-support/huskyx8-support/" style="padding-left:54px">Asistencia de Husky X8</a>
</li>
</ul>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/support/downloads/" onclick="return false;" style="padding-left:18px">Downloads</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="NewNavigation_Support" data-enable-google-event-tracking="True" data-label="Support_DownloadSoftware_es" href="/es/support/resources/download-software/" style="padding-left:36px">Descargar software</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="DownloadDrivers_es" href="/es/support/resources/download-software/?type=17&amp;lang=27" style="padding-left:36px">Descargar drivers</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="SDK_es" href="/es/comunidad/herramientas-de-desarrolladores/sdk/" style="padding-left:36px">Descargar MIP SDK</a>
</li>
<li><a href="/es/support/downloads/download-xprotect-hotfixes/" style="padding-left:36px">Download XProtect Hotfixes</a>
</li>
</ul>
</li>
<li class="active"><a class="non-clickable" href="/es/support/tools-and-references/" onclick="return false;" style="padding-left:18px">Tools &amp; References</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="SupportedDevices_Resources_es" href="/es/comunidad/herramientas-de-socios-comerciales/supported-devices/" style="padding-left:36px">Dispositivos compatibles</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="SoftwareRegistration_es" href="https://online.milestonesys.com/Account/Login?ReturnUrl=/" style="padding-left:36px" target="_blank">Registro del software</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="DevicePacks_Ressources_es" href="/es/comunidad/herramientas-de-socios-comerciales/device-packs/" style="padding-left:36px" target="_self">Paquetes de dispositivos</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="ServerCalculator_Resources_es" href="/es/my-milestone/default/xprotect-server-calculator/" style="padding-left:36px">Calculadora de servidores XProtect</a>
</li>
<li><a href="/es/support/tools-and-references/system-requirements/" style="padding-left:36px">Requisitos del sistema</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_Support_es" data-enable-google-event-tracking="True" data-label="Nav_HelpYourself_XProtect_Comparison_Tool_es" href="/es/comunidad/herramientas-de-socios-comerciales/xprotect-comparison-tools/" style="padding-left:36px">XProtect Comparison Tools</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="AEPortal_LetUsHelpYou_es" href="/es/comunidad/herramientas-de-socios-comerciales/architects-and-engineers/" style="padding-left:36px">Arquitectura e Ingenier&#237;a</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="CreateAMilestoneID_es" href="/es/login-page/create-profile/" style="padding-left:36px">Crear un ID de Milestone</a>
</li>
<li><a href="/es/support/tools-and-references/product-lifecycle/" style="padding-left:36px">Ciclo de vida del producto</a>
</li>
<li class="active"><a href="/es/support/tools-and-references/cyber-security/" style="padding-left:36px">Ciberseguridad</a>
</li>
<li><a href="/es/support/tools-and-references/compliance-and-certification/" style="padding-left:36px">Compliance &amp; Certification</a>
</li>
<li><a href="/es/support/tools-and-references/supported-languages/" style="padding-left:36px">Idiomas compatibles</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_Support" data-enable-google-event-tracking="True" data-label="InterconnectCompatibility_es" href="/es/solutions/hardware-y-add-on/productos-add-on-de-milestone/interconnect/compatibilidad-de-milestone-interconnect/" style="padding-left:36px">Compatibilidad de Interconnect</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/support/contact-us/" onclick="return false;" style="padding-left:18px">Contact Us</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/support/contact-us/license-chat/" style="padding-left:36px" target="_self">License Chat</a>
</li>
<li><a href="/es/support/contact-us/technical-support-care-portals/" style="padding-left:36px">Portales de asistencia t&#233;cnica</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Support_PresalesSupport" href="/es/support/permitanos-ayudarle/asistencia-preventa/" style="padding-left:36px">Presales Support</a>
</li>
<li><a href="/es/support/contact-us/sales-support/" style="padding-left:36px">Sales Support</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="MobileSupport_es" href="https://supportcommunity.milestonesys.com/s/my-cases" style="padding-left:36px">Asistencia m&#243;vil</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="GlobalBidDesk_LetUsHelpYou" href="/es/comunidad/herramientas-de-socios-comerciales/global-bid-desk/" style="padding-left:36px">Global Bid Desk</a>
</li>
</ul>
</li>
</ul>                        </li>
                        <li>
                            <a href="/es/events/">Eventos</a><div class="open-icon"><div class="divider"></div><div class="image"></div></div>

<ul class="menuitems"><li><a class="non-clickable" href="/es/events/upcoming-events/" onclick="return false;" style="padding-left:18px">Upcoming Events</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="UpcomingEvents_Conferences_es" href="/es/events/?ct=conference" style="padding-left:36px">Conferencia</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="UpcomingEvents_Seminars_es" href="/es/events/?ct=Seminar" style="padding-left:36px">Seminario</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="UpcomingEvents_Tradeshows_es" href="/es/events/?ct=tradeshow" style="padding-left:36px">Feria</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="UpcomingEvents_Trainings_and_Certifications_es" href="https://learn.milestonesys.com/scheduledclasses" style="padding-left:36px" target="_blank">Clases de formaci&#243;n</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="UpcomingEvents_All_upcoming _events_es" href="/es/events/?nogeo=1" style="padding-left:36px">Todos los pr&#243;ximos eventos</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/events/seminario-en-linea/" onclick="return false;" style="padding-left:18px">Seminario en l&#237;nea</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Webinars_Commercial_es" href="/es/events/?ct=webinar&amp;ct=commercial" style="padding-left:36px">Comercial</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Webinars_New_to_Milestone_es" href="/es/events/?ct=webinar&amp;ct=new_to_milestone" style="padding-left:36px">Nuevo en Milestone</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Webinars_Product_release_es" href="/es/events/?ct=webinar&amp;ct=product_release" style="padding-left:36px">Lanzamiento de productos</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Webinars_Technical_es" href="/es/events/?ct=webinar&amp;ct=technical" style="padding-left:36px">Gestor de cuenta</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Webinars_All_upcoming_webinars_es" href="/es/events/?ct=Webinar&amp;nogeo=1" style="padding-left:36px">Todos los pr&#243;ximos webinarios</a>
</li>
<li><a href="/es/events/seminario-en-linea/recorded-webinars/" style="padding-left:36px">Seminarios web grabados</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/events/digital-exp/" onclick="return false;" style="padding-left:18px">Digital Experience</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="CustomLink_MIPS2021" href="https://events.milestonesys.com/" style="padding-left:36px" target="_self">MIPS 2021</a>
</li>
<li><a href="/es/events/digital-exp/mips-2020/" style="padding-left:36px">MIPS 2020</a>
</li>
</ul>
</li>
</ul>                        </li>
                        <li>
                            <a href="/es/news/">News</a><div class="open-icon"><div class="divider"></div><div class="image"></div></div>

<ul class="menuitems"><li><a class="non-clickable" href="/es/news/sala-de-prensa/" onclick="return false;" style="padding-left:18px">Sala de prensa</a>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="TheilestoneNewsroom_Newsroom" href="/es/news/" style="padding-left:36px" target="_blank">The Milestone Newsroom</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="TheMilestonePost_es" href="http://news.milestonesys.com/" style="padding-left:36px">The Milestone Post</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="FindProductMaterials_Newsroom_es" href="https://content.milestonesys.com/" style="padding-left:36px" target="_blank">Portal de contenidos</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Sign_up_for_news" href="https://pardot.milestonesys.com/marketing-communication" style="padding-left:36px" target="_self">Sign up for news</a>
</li>
</ul>
</li>
</ul>                        </li>

                    
                    <div class="show-mobile header-links" style="height: 264px;"><a href="/es/comunidad/encuentre-un-socio-de-milestone/">D&#243;nde comprarlo</a>
<span>|</span>
<a href="/es/about-us/">Acerca de nosotros</a>
<span>|</span>
<a href="/es/about-us/career/">Carreras profesionales</a>
<span>|</span>
</div>
                </ul>
            </nav>
            <!-- /.navbar-collapse -->
                <!-- Mega menu start-->
                <div class="nav-tab-boxes show-desktop hidefirst">
                        <div class="nav-tab-box">
                            <div class="overlay">
<ul class="menuitems"><li><a class="non-clickable" href="/es/solutions/plataforma/" onclick="return false;">Plataforma</a>
<div class="underline"></div>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/solutions/plataforma/por-que-escoger-milestone/">&#191;Por qu&#233; escoger Milestone?</a>
</li>
<li><a href="/es/solutions/plataforma/video-management-software/">Software de gesti&#243;n de v&#237;deo</a>
</li>
<li><a href="/es/solutions/plataforma/XProtect-Clients/">Clientes XProtect</a>
</li>
<li><a href="/es/solutions/plataforma/xprotect-cloud-solutions/">XProtect Cloud Solutions</a>
</li>
<li><a href="/es/solutions/plataforma/indice-de-productos/">&#205;ndice de productos</a>
</li>
<li><a href="/es/solutions/plataforma/try-our-software/">Pruebe nuestro software</a>
</li>
<li><a class="googlelinktracking" data-category="DemoCampaign_es" data-enable-google-event-tracking="True" data-label="Navigation_BookAFreeVMSDemo_es" href="/es/campaigns/book-a-demo/">Reserva una demostraci&#243;n VMS gratuita</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/solutions/hardware-y-add-on/" onclick="return false;">Hardware y Add-on</a>
<div class="underline"></div>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/solutions/hardware-y-add-on/why-choose-Husky/">&#191;Por qu&#233; elegir Husky IVO?</a>
</li>
<li><a href="/es/solutions/hardware-y-add-on/HuskyIVO-series/">Dispositivos de v&#237;deo Husky IVO</a>
</li>
<li><a href="/es/solutions/hardware-y-add-on/productos-add-on-de-milestone/">Productos add-on de Milestone</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="SupportedDevices_HardwareAndAddOns_es" href="/es/comunidad/herramientas-de-socios-comerciales/supported-devices/">Dispositivos compatibles</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/solutions/services/" onclick="return false;">Servicios</a>
<div class="underline"></div>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="ServiceOverview_es" href="/es/solutions/services/">Visi&#243;n general de servicios</a>
</li>
<li><a href="/es/solutions/services/milestone-care/">Milestone Care™</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Milestone_Learning" href="https://learn.milestonesys.com/index.htm">Milestone Learning</a>
</li>
<li><a href="/es/solutions/services/customer-dashboard/">Panel del Cliente</a>
</li>
<li><a href="/es/solutions/services/servicios-profesionales/">Servicios Profesionales</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="CustomDevelopment_es" href="/es/comunidad/herramientas-de-desarrolladores/custom-development/">Custom Development</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="Nav_Services_VersionComparisonTool_es" href="/es/comunidad/herramientas-de-socios-comerciales/xprotect-comparison-tools/">Herramienta de comparaci&#243;n de versiones</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/solutions/industrias/" onclick="return false;">Industrias</a>
<div class="underline"></div>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/solutions/industrias/education/">Education</a>
</li>
<li><a href="/es/solutions/industrias/public-transportation/">Public Transportation</a>
</li>
<li><a href="/es/solutions/industrias/retail/">Retail</a>
</li>
<li><a href="/es/solutions/industrias/safe-cities/">Safe cities</a>
</li>
<li><a href="/es/solutions/industrias/transportation/">Transportation</a>
</li>
<li><a href="/es/solutions/industrias/us-federal-government/">US Federal Government</a>
</li>
</ul>
</li>
</ul>                            </div>

    <div class="navigation-banner-link col-sm-12">
        


<div style="background-image: url('https://mswebappcdn.azureedge.net/episerverprod/0903294c33fb4ac1bcc0f98da754e901/1581b1ecfea9407daa8c093e1c879ca3.jpg');" class="navigation-banner">
    <div class="container navigation-banner-container">
        <div class="row navigation-banner-row">
                <div class="bannertitle-seperator">
                        <div class="nav-title col-xs-8 col-xs-offset-2 text-color2 font-size9 font-weight-standard">
                            The Husky IVO series is out now!
                        </div>
                                            <div class="nav-description col-xs-8 col-xs-offset-2 text-color2 font-size1 font-weight-standard">
                            You can now order the entire Milestone Husky IVO™ series. Visit the new Husky IVO website to explore this latest generation of Milestone video surveillance appliances.
                        </div>
                    <div class="col-xs-8 col-xs-offset-2">
                        <div class="row buttons"><div>


<div class="buttonblock textaligncenter">
        <a target="_blank" href="/es/solutions/hardware-y-add-on/why-choose-Husky/" data-category="HuskyIVOSeries" data-label="NavBanner_Solutions_PreOrderHuskyIVO" data-enable-google-event-tracking="True" class="button hover background-color18 border-color18 googlelinktracking">
            

<span data-text-color="text-color13" data-background-color="background-color18" data-border-color="border-color18" data-hover-text-color="text-color13" data-hover-background-color="background-color38" data-hover-border-color="border-color38" data-active-text-color="text-color13" data-active-background-color="background-color37" data-active-border-color="border-color37" class="text-color13">GO CHECK IT OUT</span>
        </a>
    </div>
</div></div>
                    </div>

                </div>
        </div>
    </div>
</div>

    </div>
                        </div>
                        <div class="nav-tab-box">
                            <div class="overlay">
<ul class="menuitems"><li><a class="non-clickable" href="/es/comunidad/hagase-socio/" onclick="return false;">H&#225;gase socio</a>
<div class="underline"></div>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/comunidad/hagase-socio/la-plataforma-abierta/">La plataforma abierta</a>
</li>
<li><a href="/es/comunidad/hagase-socio/distributor/">Distribuidor</a>
</li>
<li><a href="/es/comunidad/hagase-socio/technology-partner-program/">Technology Partner Program</a>
</li>
<li><a href="/es/comunidad/hagase-socio/reseller/">Revendedor</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/comunidad/herramientas-de-desarrolladores/" onclick="return false;">Herramientas de desarrolladores</a>
<div class="underline"></div>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="DownloadSoftware_DeveloperTools_es" href="/es/support/resources/download-software/">Descargar software</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="new_DeveloperForum_DeveloperTools_es" href="http://developer.milestonesys.com/" target="_blank">Foro para desarrolladores</a>
</li>
<li><a href="/es/comunidad/herramientas-de-desarrolladores/milestone-developer-champions/">Milestone Developer Champions</a>
</li>
<li><a href="/es/comunidad/herramientas-de-desarrolladores/kickstarter-contest-2021/">Kickstarter Contest</a>
</li>
<li><a href="/es/comunidad/herramientas-de-desarrolladores/sdk/">SDK</a>
</li>
<li><a href="/es/comunidad/herramientas-de-desarrolladores/custom-development/">Custom Development</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="FindProductMaterials_DeveloperTools_es" href="https://content.milestonesys.com/" target="_blank">Portal de contenidos</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="MyMilestone_DeveloperTools_es" href="/es/my-milestone/">My Milestone</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Cybersecurity_DeveloperTools" href="/es/support/tools-and-references/cyber-security/">Cybersecurity</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/comunidad/herramientas-de-socios-comerciales/" onclick="return false;">Herramientas de socios comerciales</a>
<div class="underline"></div>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/comunidad/herramientas-de-socios-comerciales/supported-devices/">Dispositivos compatibles</a>
</li>
<li><a href="/es/comunidad/herramientas-de-socios-comerciales/device-packs/">Device Packs</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="DownloadSoftware_BusinessPartnerTools_es" href="/es/support/resources/download-software/">Descargar software</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="FindProductMaterials_BusinessPartnerTools_es" href="https://content.milestonesys.com/" target="_blank">Portal de contenidos</a>
</li>
<li><a href="/es/comunidad/herramientas-de-socios-comerciales/xprotect-comparison-tools/">XProtect Comparison Tools</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="CustomerDashboard_es" href="/es/solutions/services/customer-dashboard/">Customer Dashboard</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="ServerCalculator_BusinessPartnerTools_es" href="/es/my-milestone/default/xprotect-server-calculator/">Calculador de servidores</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="DocumentationPortal_Community_BPT" href="https://doc.milestonesys.com/?utm_source=MSweb&amp;utm_medium=Megamenu&amp;utm_campaign=Permanent" target="_self">Milestone Documentation</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="LearningAndPerformance_BusinessPartnerTools_es" href="https://learn.milestonesys.com/index.htm">Formaci&#243;n y rendimiento</a>
</li>
<li><a href="/es/comunidad/herramientas-de-socios-comerciales/global-bid-desk/">Global Bid Desk</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="MyMilestone_BusinessPartnerTools_es" href="/es/my-milestone/">My Milestone</a>
</li>
<li><a href="/es/comunidad/herramientas-de-socios-comerciales/architects-and-engineers/">Arquitectos e ingenieros</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/comunidad/marketplace/" onclick="return false;">Marketplace</a>
<div class="underline"></div>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/comunidad/marketplace/start-exploring/">Empiece a descubrir</a>
</li>
<li><a href="/es/comunidad/marketplace/what-is-marketplace/">&#191;Qu&#233; es Milestone Marketplace?</a>
</li>
<li><a href="/es/comunidad/marketplace/join-marketplace/">Join Marketplace</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="Nav_Marketplace_login_es" href="/my-milestone/marketplace/" target="_blank">Iniciar sesi&#243;n en Marketplace</a>
</li>
<li><a href="/es/comunidad/marketplace/support/">Marketplace Support</a>
</li>
</ul>
</li>
</ul>                            </div>
                        </div>
                        <div class="nav-tab-box">
                            <div class="overlay">
<ul class="menuitems"><li><a class="non-clickable" href="/es/milestone-marketplace/milestone-marketplace/" onclick="return false;">Milestone Marketplace</a>
<div class="underline"></div>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="Marketplace_Main_Nav_es" data-enable-google-event-tracking="True" data-label="MP_Start_Exploring_Second_Level_es" href="/es/comunidad/marketplace/start-exploring/" target="_self">Empiece a descubrir</a>
</li>
<li><a class="googlelinktracking" data-category="Marketplace_Main_Nav_es" data-enable-google-event-tracking="True" data-label="MP_What_is_MP_es" href="/es/under-construction/lavinia/what-is-marketplace/" target="_self">&#191;En qu&#233; consiste Marketplace?</a>
</li>
<li><a class="googlelinktracking" data-category="Marketplace_Main_Nav_es" data-enable-google-event-tracking="True" data-label="MP_Join_Milestone_es" href="/es/under-construction/lavinia/join-marketplace/" target="_self">&#218;nase a Marketplace</a>
</li>
<li><a class="googlelinktracking" data-category="Marketplace_Main_Nav_es" data-enable-google-event-tracking="True" data-label="MP_Marketplace Login_es" href="/es/my-milestone/marketplace/" target="_self">Iniciar sesi&#243;n en Marketplace</a>
</li>
<li><a class="googlelinktracking" data-category="Marketplace_Main_Nav_es" data-enable-google-event-tracking="True" data-label="MP_Marketplace_Support_es" href="/es/comunidad/marketplace/support/" target="_self">Asistencia de Marketplace</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/milestone-marketplace/challenges/" onclick="return false;">Challenges</a>
<div class="underline"></div>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/milestone-marketplace/challenges/understand-customer-behavior/">Understand customer behavior</a>
</li>
<li><a href="/es/milestone-marketplace/challenges/prevent-vandalism/">Prevent Vandalism</a>
</li>
<li><a href="/es/milestone-marketplace/challenges/gather-evidence/">Gather evidence for criminal investigations</a>
</li>
<li><a href="/es/milestone-marketplace/challenges/respond-to-medical-emergencies/">Respond to medical emergencies</a>
</li>
<li><a href="/es/milestone-marketplace/challenges/control-access-to-restricted-areas/">Control access to restricted areas</a>
</li>
<li><a href="/es/milestone-marketplace/challenges/provide-situational-awareness/">Provide situational awareness</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/milestone-marketplace/areas-of-practice/" onclick="return false;">Areas of practice</a>
<div class="underline"></div>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/milestone-marketplace/areas-of-practice/central-monitoring/">Central Monitoring</a>
</li>
<li><a href="/es/milestone-marketplace/areas-of-practice/surveillance/">Surveillance</a>
</li>
<li><a href="/es/milestone-marketplace/areas-of-practice/access-control/">Access Control</a>
</li>
<li><a href="/es/milestone-marketplace/areas-of-practice/investigation/">Investigation</a>
</li>
<li><a href="/es/milestone-marketplace/areas-of-practice/tracking-monitoring/">Tracking &amp; Monitoring</a>
</li>
<li><a href="/es/milestone-marketplace/areas-of-practice/detection/">Detection</a>
</li>
<li><a href="/es/milestone-marketplace/areas-of-practice/intrusion-alarm/">Intrusion &amp; Alarm</a>
</li>
<li><a href="/es/milestone-marketplace/areas-of-practice/vehicles-traffic/">Vehicles &amp; Traffic</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/milestone-marketplace/technologies/" onclick="return false;">Technologies</a>
<div class="underline"></div>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/milestone-marketplace/technologies/facial-recognition/">Facial Recognition</a>
</li>
<li><a href="/es/milestone-marketplace/technologies/voice-recognition/">Voice Recognition</a>
</li>
<li><a href="/es/milestone-marketplace/technologies/smoke-detection/">Smoke Detection</a>
</li>
<li><a href="/es/milestone-marketplace/technologies/motion-detection/">Motion Detection</a>
</li>
<li><a href="/es/milestone-marketplace/technologies/GPS-tracking/">GPS Tracking</a>
</li>
<li><a href="/es/milestone-marketplace/technologies/access-control/">Access Control</a>
</li>
<li><a href="/es/milestone-marketplace/technologies/GIS/">GIS</a>
</li>
<li><a href="/es/milestone-marketplace/technologies/ANPR/">ANPR</a>
</li>
<li><a href="/es/milestone-marketplace/technologies/body-worn-solutions/">Body-Worn Solutions</a>
</li>
</ul>
</li>
</ul>                            </div>
                        </div>
                        <div class="nav-tab-box">
                            <div class="overlay">
<ul class="menuitems"><li><a class="non-clickable" href="/es/support/self-service-and-support/" onclick="return false;">Self-Service &amp; Support</a>
<div class="underline"></div>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="KnowledgeBase_es" href="https://supportcommunity.milestonesys.com/s/knowledgebase" target="_blank">Base de conocimientos</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="SupportCommunity_es" href="https://supportcommunity.milestonesys.com/s/" target="_blank">Comunidad de Asistencia</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="new_DeveloperForum_HelpYourself_es" href="http://developer.milestonesys.com/" target="_blank">Foro para desarrolladores</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="eLearning_es" href="https://learn.milestonesys.com/index.htm">Portal de formaci&#243;n</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Nav_HelpYourself_ DeploymentAssistant" href="https://www.milestonesys.com/deployment-assistant" target="_blank">Milestone Deployment Assistant</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Nav_SelfServiceandSupport_ DocumentationPortal" href="https://doc.milestonesys.com/?utm_source=MSweb&amp;utm_medium=Megamenu&amp;utm_campaign=Permanent" target="_self">Milestone Documentation</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="WhitePapers_es" href="https://content.milestonesys.com/search/set/?resetsearch&amp;field=metaproperty_Assettype&amp;value=Whitepaper&amp;multiple=false&amp;filterType=add&amp;filterkey=savedFilters" target="_blank">Documentos t&#233;cnicos</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_Support" data-enable-google-event-tracking="True" data-label="ContentPortal" href="https://content.milestonesys.com/">Content Portal</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_Support" data-enable-google-event-tracking="True" data-label="SupportWebinars_es" href="/es/events/">Seminarios web de asistencia</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="XProtectEssentialSupport_es" href="/es/solutions/plataforma/video-management-software/xprotect-essential/ayuda-de-essential2/">Asistencia de XProtect Essential+</a>
</li>
<li><a href="/es/support/self-service-and-support/husky-support/">Asistencia Husky serie X</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/support/downloads/" onclick="return false;">Downloads</a>
<div class="underline"></div>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="NewNavigation_Support" data-enable-google-event-tracking="True" data-label="Support_DownloadSoftware_es" href="/es/support/resources/download-software/">Descargar software</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="DownloadDrivers_es" href="/es/support/resources/download-software/?type=17&amp;lang=27">Descargar drivers</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="SDK_es" href="/es/comunidad/herramientas-de-desarrolladores/sdk/">Descargar MIP SDK</a>
</li>
<li><a href="/es/support/downloads/download-xprotect-hotfixes/">Download XProtect Hotfixes</a>
</li>
</ul>
</li>
<li class="active"><a class="non-clickable" href="/es/support/tools-and-references/" onclick="return false;">Tools &amp; References</a>
<div class="underline"></div>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="SupportedDevices_Resources_es" href="/es/comunidad/herramientas-de-socios-comerciales/supported-devices/">Dispositivos compatibles</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="SoftwareRegistration_es" href="https://online.milestonesys.com/Account/Login?ReturnUrl=/" target="_blank">Registro del software</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="DevicePacks_Ressources_es" href="/es/comunidad/herramientas-de-socios-comerciales/device-packs/" target="_self">Paquetes de dispositivos</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="ServerCalculator_Resources_es" href="/es/my-milestone/default/xprotect-server-calculator/">Calculadora de servidores XProtect</a>
</li>
<li><a href="/es/support/tools-and-references/system-requirements/">Requisitos del sistema</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_Support_es" data-enable-google-event-tracking="True" data-label="Nav_HelpYourself_XProtect_Comparison_Tool_es" href="/es/comunidad/herramientas-de-socios-comerciales/xprotect-comparison-tools/">XProtect Comparison Tools</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="AEPortal_LetUsHelpYou_es" href="/es/comunidad/herramientas-de-socios-comerciales/architects-and-engineers/">Arquitectura e Ingenier&#237;a</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="CreateAMilestoneID_es" href="/es/login-page/create-profile/">Crear un ID de Milestone</a>
</li>
<li><a href="/es/support/tools-and-references/product-lifecycle/">Ciclo de vida del producto</a>
</li>
<li class="active"><a href="/es/support/tools-and-references/cyber-security/">Ciberseguridad</a>
</li>
<li><a href="/es/support/tools-and-references/compliance-and-certification/">Compliance &amp; Certification</a>
</li>
<li><a href="/es/support/tools-and-references/supported-languages/">Idiomas compatibles</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_Support" data-enable-google-event-tracking="True" data-label="InterconnectCompatibility_es" href="/es/solutions/hardware-y-add-on/productos-add-on-de-milestone/interconnect/compatibilidad-de-milestone-interconnect/">Compatibilidad de Interconnect</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/support/contact-us/" onclick="return false;">Contact Us</a>
<div class="underline"></div>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a href="/es/support/contact-us/license-chat/" target="_self">License Chat</a>
</li>
<li><a href="/es/support/contact-us/technical-support-care-portals/">Portales de asistencia t&#233;cnica</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Support_PresalesSupport" href="/es/support/permitanos-ayudarle/asistencia-preventa/">Presales Support</a>
</li>
<li><a href="/es/support/contact-us/sales-support/">Sales Support</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="MobileSupport_es" href="https://supportcommunity.milestonesys.com/s/my-cases">Asistencia m&#243;vil</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="GlobalBidDesk_LetUsHelpYou" href="/es/comunidad/herramientas-de-socios-comerciales/global-bid-desk/">Global Bid Desk</a>
</li>
</ul>
</li>
</ul>                            </div>
                        </div>
                        <div class="nav-tab-box">
                            <div class="overlay">
<ul class="menuitems"><li><a class="non-clickable" href="/es/events/upcoming-events/" onclick="return false;">Upcoming Events</a>
<div class="underline"></div>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="UpcomingEvents_Conferences_es" href="/es/events/?ct=conference">Conferencia</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="UpcomingEvents_Seminars_es" href="/es/events/?ct=Seminar">Seminario</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="UpcomingEvents_Tradeshows_es" href="/es/events/?ct=tradeshow">Feria</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="UpcomingEvents_Trainings_and_Certifications_es" href="https://learn.milestonesys.com/scheduledclasses" target="_blank">Clases de formaci&#243;n</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="UpcomingEvents_All_upcoming _events_es" href="/es/events/?nogeo=1">Todos los pr&#243;ximos eventos</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/events/seminario-en-linea/" onclick="return false;">Seminario en l&#237;nea</a>
<div class="underline"></div>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Webinars_Commercial_es" href="/es/events/?ct=webinar&amp;ct=commercial">Comercial</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Webinars_New_to_Milestone_es" href="/es/events/?ct=webinar&amp;ct=new_to_milestone">Nuevo en Milestone</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Webinars_Product_release_es" href="/es/events/?ct=webinar&amp;ct=product_release">Lanzamiento de productos</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Webinars_Technical_es" href="/es/events/?ct=webinar&amp;ct=technical">Gestor de cuenta</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Webinars_All_upcoming_webinars_es" href="/es/events/?ct=Webinar&amp;nogeo=1">Todos los pr&#243;ximos webinarios</a>
</li>
<li><a href="/es/events/seminario-en-linea/recorded-webinars/">Seminarios web grabados</a>
</li>
</ul>
</li>
<li><a class="non-clickable" href="/es/events/digital-exp/" onclick="return false;">Digital Experience</a>
<div class="underline"></div>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="CustomLink_MIPS2021" href="https://events.milestonesys.com/" target="_self">MIPS 2021</a>
</li>
<li><a href="/es/events/digital-exp/mips-2020/">MIPS 2020</a>
</li>
</ul>
</li>
</ul>                            </div>

    <div class="navigation-banner-link col-sm-12">
        


<div style="background-image: url('https://mswebappcdn.azureedge.net/episerverprod/ba1370f28e8647888d55a9fc42a69e06/7cdec7faa69d4d79b4fc1b0d806a2e1f.jpg');" class="navigation-banner">
    <div class="container navigation-banner-container">
        <div class="row navigation-banner-row">
                <div class="bannertitle-seperator">
                        <div class="nav-title col-xs-8 col-xs-offset-2 text-color2 font-size9 font-weight-standard">
                            It's a wrap on MIPS 2021!
                        </div>
                                            <div class="nav-description col-xs-8 col-xs-offset-2 text-color2 font-size1 font-weight-standard">
                            Watch all the conference and on-demand sessions at MIPS OnDemand – there’s so much free content to explore. Dive in and start shaping your new next!
                        </div>
                    <div class="col-xs-8 col-xs-offset-2">
                        <div class="row buttons"><div class="col-xs-12 col-12">


<div class="buttonblock textaligncenter">
        <a target="_self" href="https://events.milestonesys.com/" data-category="MIPS2021" data-label="NavBanner_Events_button" data-enable-google-event-tracking="True" class="button hover background-color18 border-color18 googlelinktracking">
            

<span data-text-color="text-color13" data-background-color="background-color18" data-border-color="border-color18" data-hover-text-color="text-color13" data-hover-background-color="background-color38" data-hover-border-color="border-color38" data-active-text-color="text-color13" data-active-background-color="background-color37" data-active-border-color="border-color37" class="text-color13">WATCH NOW</span>
        </a>
    </div>
</div></div>
                    </div>

                </div>
        </div>
    </div>
</div>

    </div>
                        </div>
                        <div class="nav-tab-box">
                            <div class="overlay">
<ul class="menuitems"><li><a class="non-clickable" href="/es/news/sala-de-prensa/" onclick="return false;">Sala de prensa</a>
<div class="underline"></div>
<div class="open-icon"><div class="divider"></div>
<div class="image"></div>
</div>
<ul class="menuitems"><li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="TheilestoneNewsroom_Newsroom" href="/es/news/" target="_blank">The Milestone Newsroom</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="TheMilestonePost_es" href="http://news.milestonesys.com/">The Milestone Post</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation_es" data-enable-google-event-tracking="True" data-label="FindProductMaterials_Newsroom_es" href="https://content.milestonesys.com/" target="_blank">Portal de contenidos</a>
</li>
<li><a class="googlelinktracking" data-category="NewNavigation" data-enable-google-event-tracking="True" data-label="Sign_up_for_news" href="https://pardot.milestonesys.com/marketing-communication" target="_self">Sign up for news</a>
</li>
</ul>
</li>
</ul>                            </div>
                        </div>
                    <div class="shadow"></div>
                </div>
                <!-- Mega menu end-->
        </div>


</div></div></div> 

</div>
<div class="container-fluid">
    

    
<div class="row"><div class="tile custom-background-image full-background-image no-margin-bottom col-xs-12 col-12" data-backgroundimage="https://mswebappcdn.azureedge.net/episerverprod/7e7e3fda4aac433790ac88ac8f12067a/65399da765ee4b35a60d73515be514cc.jpg" data-backgroundimagebreakpoint="" style="background-image: url(https://mswebappcdn.azureedge.net/episerverprod/7e7e3fda4aac433790ac88ac8f12067a/65399da765ee4b35a60d73515be514cc.jpg);">



    <div         class="container"
>
        <div class="row">
            <div         class="col-xs-12 col-12"
>
                







        <div class="title textaligncenter">
            


    <span         class="textblock  font-weight-standard font-size9 textaligncenter"
        style="color: #ffffff;"
><br /><br /><br /><br /><br />Seguridad proactiva del sistema</span>

        </div>










    <div class="row">
        <div         class="col-xs-12"
>
            <div         class="description textaligncenter"
><p><span style="color: #ffffff;">Si sospecha de una vulnerabilidad de seguridad en un producto/servicio de Milestone, informe del problema inmediatamente.<br />Milestone responderá en 48 horas.</span></p></div>
        </div>
    </div>



    <div         class="links textaligncenter"
>



<div class="buttonblock textaligncenter">
        <a target="_self" href="mailto:cybersecurity@milestonesys.com" data-category="Cybersecurity" data-label="ContactUs" data-enable-google-event-tracking="True" class="button hover background-color18 border-color18 googlelinktracking">
            

<span data-text-color="text-color13" data-background-color="background-color18" data-border-color="border-color18" data-hover-text-color="text-color13" data-hover-background-color="background-color38" data-hover-border-color="border-color38" data-active-text-color="text-color13" data-active-background-color="background-color37" data-active-border-color="border-color37" class="text-color13">CONTÁCTEN.</span>
        </a>
    </div>
    </div>

            </div>
        </div>
    </div>
</div><div class="tile col-xs-12 col-12">



    <div         class="container"
>
        <div class="row">
            <div         class="col-xs-12 col-12"
>
                








<div class="media textaligncenter top-vertical-alignment">
        <img src="https://mswebappcdn.azureedge.net/episerverprod/29e805309098459bab875aa11aa2baf4/23b2179e1d7241958d65be6fe819bdc7.png" alt="" loading="lazy"/>
</div>



        <div class="title textaligncenter">
            


    <span         class="textblock  font-weight-light font-size9 textaligncenter"
>Qué podemos hacer para ayudar<br /><br /></span>

        </div>










    <div class="row">
        <div         class="col-xs-10 col-xs-push-1 col-sm-8 col-sm-push-2"
>
            <div         class="description textaligncenter"
><p style="text-align: center;">Garantizar la seguridad e integridad de todas las instalaciones Milestone será siempre una prioridad para nosotros. Use esta página para obtener más datos o para contactar si sospecha que hay algún problema de ciberseguridad Minimice exposiciones de clientes a riesgos garantizando que nuestro software y hardware están securizados por diseño, seguros de forma predeterminada y seguros en su instalación.</p>
<p style="text-align: center;">Si detecta un fallo en la vulnerabilidad, Milestone ofrecerá una sulucion o actualización en el software tan pronto como sea posible con correcceciones de seguridad para clientes y socios, gratis, siempre y cuando el producto siga siendo compatible</p></div>
        </div>
    </div>




            </div>
        </div>
    </div>
</div><div class="tile custom-background-color no-margin-bottom col-xs-12 col-12" style="background-color: #f1f1f0;padding-top: 50px;">



    <div         class="container"
>
        <div class="row">
            <div         class="col-xs-12 col-12"
>
                







        <div class="title textaligncenter">
            


    <span         class="textblock  font-weight-light font-size9 textaligncenter"
>Para obtener más información sobre las vulnerabilidades recientes y cómo resolverlas, consulte nuestros artículos sobre ciberseguridad.</span>

        </div>



        <div class="title textaligncenter">
            


    <span         class="textblock  font-weight-standard font-size6 textaligncenter"
>Descubra la Milestone Husky que satisface sus necesidades</span>

        </div>









    <div         class="contentarea textalignleft"
><div class="row"><div class="gridtile col-xs-12 col-12">








<script type="text/javascript">
    defer(function () {

        var tableName = "#gridStandard_" + 98446;
        var table = $("#gridStandard_" + 98446);
        var filetitle='';
        var searchText='Buscar aqu&#237;...';
        var exportAsPdf='Exportar como PDF';
        var exportAsExcel='Exportar como Excel';
        var tableOptions = {
            responsive: true,
            lengthMenu: [[5,10, 20, 30, 40,50, -1], [5,10, 20, 30, 40,50, "All"]],
            dom:'<"top"fl>rt<"bottom"pB><"clear">',
            sPaginationType: "full_numbers,",
            pagingType: "input",
            pageLength:5,
            paging: true,
            language: {
                "lengthMenu": "Page Size _MENU_",
                "search": "_INPUT_",
                "searchPlaceholder": searchText
            },
            buttons: [{
                "title": filetitle,
                "extend": 'excel',
                "text": exportAsExcel

            },{
                "title": filetitle,
                "extend": 'pdf',
                "text": exportAsPdf

            }]
        }

        var tables=  table.DataTable(tableOptions);


        $(tableName+' tbody')
      .on( 'mouseenter', 'tr', function () {
          tables.$('td.highlight').removeClass('highlight');
          $('td', $(this)).addClass('highlight');
      } );

        $(tableName + ' tbody').mouseleave(function () {
            $('td.highlight', $(this)).removeClass('highlight');
        });

        if (false == false) {
            table.DataTable().destroy();
            tableOptions.pageLength = -1;
            table.DataTable(tableOptions);
            $(tableName+"_length").css({ "display": 'none' });
        }

        if (false == false) {
            $(tableName +"_filter").css({ "display": "none" });
        }

        if (false == false) {
            $("th", table).removeClass('sorting');
            $("th", table).removeClass('sorting_asc');
            $("th", table).removeClass('sorting_desc');
            $("th", table).unbind('click');
        }

        if (false == false) {
            $("td:nth-child(2)", table).css({ "border-left": '0' });
            $("td:last-child", table).css({ "border-right": '0' });
            $("th:nth-child(2)", table).css({ "border-left": '0' });
            $("th:last-child", table).css({ "border-right": '0' });
        }
        else {
            table.css({"border": "1px solid #c7c6c6 !important"});
        }

        if (false==false) {
            $(tableName+"_wrapper .dt-buttons .buttons-excel").css({ "display": 'none' });
        }
        else {
            $(tableName+"_wrapper .dt-buttons .buttons-excel").addClass('');
            $(tableName+"_wrapper .dt-buttons .buttons-excel span").addClass('');
        }

        if (false == false) {
            $(tableName + "_wrapper .dt-buttons .buttons-pdf").css({ "display": 'none' });
        } else {
            $(tableName + "_wrapper .dt-buttons .buttons-pdf").addClass('');
            $(tableName + "_wrapper .dt-buttons .buttons-pdf span").addClass('');
        }
        if ((false == false)&&(false == false))  {
            $(tableName + "_wrapper .dt-buttons").css({ "display": 'none' });
        }

        $(".paginate_button", table).click(function(event) {
            document.location.href = "#gridtile_" + 98446;
        });
    });
</script>

<div id="gridtile_98446" class="gridtile background-color0">

    

        <table id="gridStandard_98446" class="col-xs-12">
                <thead>
                    <tr>
                        <th style="display: none"></th>
                                    <th         class=" header-title background-color1 text-color2 font-size4 font-weight-standard textaligncenter"
>
                                        Tema del artículo
                                    </th>
                                    <th         class=" header-title background-color1 text-color2 font-size4 font-weight-standard textaligncenter"
>
                                        Productos afectados
                                    </th>
                                    <th         class=" header-title background-color1 text-color2 font-size4 font-weight-standard textaligncenter"
>
                                        Fecha de publicación
                                    </th>
                                    <th         class=" header-title background-color1 text-color2 font-size4 font-weight-standard textaligncenter"
>
                                        Artículo completo
                                    </th>
                    </tr>
                </thead>
            <tbody>
                        <tr         class="tableRow text-color6 font-size1 font-weight-thicker-standard"
>

                            <td style="display: none">1</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Tema del art&#237;culo">Vulnerabilidad de seguridad de Milestone Open Network Bridge (ONVIF)</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Productos afectados">Versiones compatibles de XProtect Open Network Bridge (2018 R2 - 2020 R3)</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Fecha de publicaci&#243;n">13 de abril de 2021</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Art&#237;culo completo"><a class="link googlelinktracking" href="https://supportcommunity.milestonesys.com/SCRedir?art=000031967&lang=en_US" target="_blank" data-category="Cybersecurity" data-label="ONVIF-security-vulnerability_es" data-enable-google-event-tracking="True">Leer más</a></td>
                        </tr>
                        <tr         class="tableRow text-color6 font-size1 font-weight-thicker-standard"
>

                            <td style="display: none">2</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Tema del art&#237;culo">XProtect Smart Client - nombre de usuario HTTP para el puerto 80</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Productos afectados">XProtect Smart Client 2020 R2 (20.2a) o anterior</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Fecha de publicaci&#243;n">10 de agosto de2020</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Art&#237;culo completo"><a class="link googlelinktracking" href="https://supportcommunity.milestonesys.com/s/article/Smart-Client-usernames-may-appear-in-plain-text-on-HTTP-port-80-hotfixes?language=en_US" target="_blank" data-category="Cybersecurity" data-label="XprotectSmartClient-username-on-HTTPport80_es" data-enable-google-event-tracking="True">Leer más</a></td>
                        </tr>
                        <tr         class="tableRow text-color6 font-size1 font-weight-thicker-standard"
>

                            <td style="display: none">3</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Tema del art&#237;culo">El panel de usuario cesará el soporte para protocolos heredados SSL/TLS</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Productos afectados">XProtect Corporate, Expert, Enterprise, Professional, Express, Essential, Go, 2016. Milestone Husky M10 (Arcus 1.0), M30 S, M50 S, M50 Advanced, M500 Advanced 2016</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Fecha de publicaci&#243;n">10 de julio de 2020</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Art&#237;culo completo"><a class="link googlelinktracking" href="https://supportcommunity.milestonesys.com/SCRedir?art=000024207&lang=en_US" target="_blank" data-category="Cybersecurity" data-label="CustomerDashboardDiscontinuesSupport_es" data-enable-google-event-tracking="True">Leer más</a></td>
                        </tr>
                        <tr         class="tableRow text-color6 font-size1 font-weight-thicker-standard"
>

                            <td style="display: none">4</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Tema del art&#237;culo">Vulnerabilidad de ejecución de XProtect Smart Client</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Productos afectados">XProtect Smart Client</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Fecha de publicaci&#243;n">11 de octubre de 2019</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Art&#237;culo completo"><a class="link googlelinktracking" href="https://supportcommunity.milestonesys.com/s/article/XProtect-Smart-Client-script-execution-vulnerability?language=en_US" target="_blank" data-category="Cybersecurity" data-label="SmartClientExecutionVulnerability_es" data-enable-google-event-tracking="True">Leer más</a></td>
                        </tr>
                        <tr         class="tableRow text-color6 font-size1 font-weight-thicker-standard"
>

                            <td style="display: none">5</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Tema del art&#237;culo">Vulnerabilidad de seguridad de la API de configuración de XProtect y solución</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Productos afectados">Versiones 2016 R1 (10.a) a 2019 R1 (13.1a) de XProtect Corporate, Expert, Professional+, Express+ y Essential+</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Fecha de publicaci&#243;n">22 de marzo de 2019</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Art&#237;culo completo"><a class="link googlelinktracking" title="Vulnerabilidad de seguridad de la API de configuración de XProtect y solución" href="https://supportcommunity.milestonesys.com/s/article/XProtect-Configuration-API-security-vulnerability-and-mitigation?language=en_US" target="_blank" data-category="Cybersecurity" data-label="XProtect Configuration API security vulnerability and mitigation_es" data-enable-google-event-tracking="True">Leer más</a></td>
                        </tr>
                        <tr         class="tableRow text-color6 font-size1 font-weight-thicker-standard"
>

                            <td style="display: none">6</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Tema del art&#237;culo">Vulnerabilidad de seguridad potencial de .NET Framework Remoting</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Productos afectados">XProtect Corporate, Expert, Professional+, Express+ y Essential+</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Fecha de publicaci&#243;n">25 de abril de 2018</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Art&#237;culo completo"><a class="link googlelinktracking" href="https://supportcommunity.milestonesys.com/s/article/XProtect-VMS-NET-security-vulnerability-hotfixes-for-2016-R1-2018-R1?language=en_US" target="_blank" data-category="Cybersecurity" data-label="NETFrameworkRemotingPotentialSecurityVulnerability_es" data-enable-google-event-tracking="True">Leer más</a></td>
                        </tr>
                        <tr         class="tableRow text-color6 font-size1 font-weight-thicker-standard"
>

                            <td style="display: none">7</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Tema del art&#237;culo">Versión de MSXML no compatible en VMS XProtect</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Productos afectados">Todo</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Fecha de publicaci&#243;n">16 de enero de 2018</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Art&#237;culo completo"><a class="link googlelinktracking" title="Leer más" href="https://supportcommunity.milestonesys.com/s/article/Unsupported-MSXML-version-in-XProtect-VMS?language=en_US" target="_blank" data-label="UnsupportedMSXMLXProtect_es" data-enable-google-event-tracking="True" data-category="Cybersecurity">Leer más</a></td>
                        </tr>
                        <tr         class="tableRow text-color6 font-size1 font-weight-thicker-standard"
>

                            <td style="display: none">8</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Tema del art&#237;culo">Ataques Meltdown y Spectre</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Productos afectados">Todos los sistemas operativos</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Fecha de publicaci&#243;n">5 de enero de 2018</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Art&#237;culo completo"><a class="link googlelinktracking" title="Leer más" href="https://supportcommunity.milestonesys.com/s/article/Meltdown-and-Spectre-attacks?language=en_US" target="_blank" data-label="MeltdownSpectreAttacks_es" data-enable-google-event-tracking="True" data-category="Cybersecurity">Leer más</a></td>
                        </tr>
                        <tr         class="tableRow text-color6 font-size1 font-weight-thicker-standard"
>

                            <td style="display: none">9</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Tema del art&#237;culo">CCleaner 5.33 Malware</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Productos afectados">Sistema operativo Windows</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Fecha de publicaci&#243;n">20 de septiembre de 2017</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Art&#237;culo completo"><a class="link googlelinktracking" title="Leer más" href="https://supportcommunity.milestonesys.com/s/article/CCleaner-Malware?language=en_US" target="_blank" data-label="CCleanerMalware_es" data-enable-google-event-tracking="True" data-category="Cybersecurity">Leer más</a></td>
                        </tr>
                        <tr         class="tableRow text-color6 font-size1 font-weight-thicker-standard"
>

                            <td style="display: none">10</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Tema del art&#237;culo">Cómo identificar y eliminar la cuenta predeterminada de usuario básico de XProtect</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Productos afectados">XProtect<sup>®</sup> Express 2017 R1 (11.1a) y versiones anteriores, XProtect<sup>®</sup> Essential 2.0 2017 R1</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Fecha de publicaci&#243;n">29 de agosto de 2017</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Art&#237;culo completo"><a class="link googlelinktracking" title="Cómo identificar y eliminar la cuenta predeterminada de usuario básico de XProtect" href="https://supportcommunity.milestonesys.com/s/article/How-to-identify-and-remove-default-XProtect-Basic-User-account?language=en_US" target="_blank" data-label="HowToIdentifyAndRemoveDefaultXProtectBasicUserAccount_es" data-enable-google-event-tracking="True" data-category="Cybersecurity">Leer más</a></td>
                        </tr>
                        <tr         class="tableRow text-color6 font-size1 font-weight-thicker-standard"
>

                            <td style="display: none">11</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Tema del art&#237;culo">Problema de ampliación de privilegios de Husky M10</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Productos afectados">Milestone Husky M10</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Fecha de publicaci&#243;n">21 de agosto de 2017</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Art&#237;culo completo"><a class="link googlelinktracking" title="Problema de ampliación de privilegios de Husky M10" href="https://supportcommunity.milestonesys.com/s/article/Husky-M10-privilege-escalation-issue?language=en_US" target="_blank" data-label="HuskyM10PriviledgeEscalationIssue_es" data-enable-google-event-tracking="True" data-category="Cybersecurity">Leer más</a></td>
                        </tr>
                        <tr         class="tableRow text-color6 font-size1 font-weight-thicker-standard"
>

                            <td style="display: none">12</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Tema del art&#237;culo">Vulnerabilidad de seguridad potencial de ONVIF</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Productos afectados">Genivia gSOAP Toolkit versiones 2.7 a 2.8.47</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Fecha de publicaci&#243;n">7 de julio de 2017</td>
                                    <td         class="tableColumn textaligncenter"
 data-label="Art&#237;culo completo"><a class="link googlelinktracking" title="Vulnerabilidad de seguridad potencial de ONVIF" href="https://supportcommunity.milestonesys.com/s/article/ONVIF-potential-security-vulnerability?language=en_US" target="_blank" data-label="ONVIFPotentialSecurityVulnerability_es" data-enable-google-event-tracking="True" data-category="Cybersecurity">Leer más</a></td>
                        </tr>
            </tbody>


        </table>
        <div class="table-footer">

        </div>
</div>
</div></div></div>


            </div>
        </div>
    </div>
</div><div class="tile col-xs-12 col-12" style="padding-top: 50px;">



    <div         class="container"
>
        <div class="row">
            <div         class="col-xs-12 col-12"
>
                







        <div class="title textaligncenter">
            


    <span         class="textblock  font-weight-light font-size9 textaligncenter"
>Descubra más información sobre la seguridad del sistema Milestone<br /><br /></span>

        </div>










    <div class="row">
        <div         class="col-xs-12"
>
            <div         class="description textaligncenter"
><p style="text-align: center;"><span style="font-size: 20px;">Estos documentos le ayudarán a elegir e implementar el nivel correcto de seguridad para su sistema:</span></p></div>
        </div>
    </div>


    <div         class="contentarea textaligncenter"
><div class="row"><div class="mediatile col-xs-12 col-12 col-sm-4">











    <div id="mediatileblock86786" class="mediatileblock textaligncenter">

        <div class="thumb"  >
                <a         class="googlelinktracking"
        data-category="Cybersecurity"
        data-enable-google-event-tracking="True"
        data-label="MilestoneCyberSecurityDevelopmentPolicy"
    target="_blank"
                href="https://mswebappcdn.azureedge.net/episerverprod/6cb5b0aab787446db6a31356272b0d09/bb704e99c2a74c4b99df1be52546f386.pdf"
>
    <picture>
        <!-- Use HTML conditional comments, to check the browser - https://scottjehl.github.io/picturefill/examples/demo-02.html -->
        <!--[if IE 9]><video style="display: none;"><![endif]-->
        <source srcset="" media="(max-width: 576px)">
        <!--[if IE 9]></video><![endif]-->

        <img src="https://mswebappcdn.azureedge.net/episerverprod/21127b5db24e4fe5ace40080a368ad27/3cd15664360b4056a737bc5048ae8386.png" style="width:auto;"  loading="lazy">
    </picture>




                </a>
        </div>

        <div         class="title"
        style="color: #009cde;"
>
                <a         class="font-size1 font-weight-standard googlelinktracking"
        data-category="Cybersecurity"
        data-enable-google-event-tracking="True"
        data-label="MilestoneCyberSecurityDevelopmentPolicy"
    target="_blank"
                href="https://mswebappcdn.azureedge.net/episerverprod/6cb5b0aab787446db6a31356272b0d09/bb704e99c2a74c4b99df1be52546f386.pdf"
>
                    


    <span         class="textblock  font-weight-standard font-size1 textaligncenter"
        style="color: #009cde;"
>Política de desarrollo de ciberseguridad Milestone</span>

                </a>
        </div>





            </div>

</div><div class="mediatile col-xs-12 col-12 col-sm-4">











    <div id="mediatileblock86670" class="mediatileblock textaligncenter">

        <div class="thumb"  >
                <a         class="googlelinktracking"
        data-category="Cybersecurity"
        data-enable-google-event-tracking="True"
        data-label="SystemSecurityFeatureBrief"
    target="_blank"
                href="https://content.milestonesys.com/l/220fd83c25afc4e2/"
>
    <picture>
        <!-- Use HTML conditional comments, to check the browser - https://scottjehl.github.io/picturefill/examples/demo-02.html -->
        <!--[if IE 9]><video style="display: none;"><![endif]-->
        <source srcset="" media="(max-width: 576px)">
        <!--[if IE 9]></video><![endif]-->

        <img src="https://mswebappcdn.azureedge.net/episerverprod/21127b5db24e4fe5ace40080a368ad27/3cd15664360b4056a737bc5048ae8386.png" style="width:auto;"  loading="lazy">
    </picture>




                </a>
        </div>

        <div         class="title"
        style="color: #009cde;"
>
                <a         class="font-size1 font-weight-standard googlelinktracking"
        data-category="Cybersecurity"
        data-enable-google-event-tracking="True"
        data-label="SystemSecurityFeatureBrief"
    target="_blank"
                href="https://content.milestonesys.com/l/220fd83c25afc4e2/"
>
                    


    <span         class="textblock  font-weight-standard font-size1 textaligncenter"
        style="color: #009cde;"
>Información de sistemas seguridad de VMS Milestone XProtect®</span>

                </a>
        </div>





            </div>

</div><div class="mediatile col-xs-12 col-12 col-sm-4">











    <div id="mediatileblock86672" class="mediatileblock textaligncenter">

        <div class="thumb"  >
                <a         class="googlelinktracking"
        data-category="Cybersecurity"
        data-enable-google-event-tracking="True"
        data-label="HardeningGuide"
    target="_blank"
                href="https://doc.milestonesys.com/2020r1/en-US/portal/htm/chapter-page-hardening-guide.htm?tocpath=Tools &amp; Architecture|XProtect VMS hardening guide|_____0"
>
    <picture>
        <!-- Use HTML conditional comments, to check the browser - https://scottjehl.github.io/picturefill/examples/demo-02.html -->
        <!--[if IE 9]><video style="display: none;"><![endif]-->
        <source srcset="" media="(max-width: 576px)">
        <!--[if IE 9]></video><![endif]-->

        <img src="https://mswebappcdn.azureedge.net/episerverprod/21127b5db24e4fe5ace40080a368ad27/3cd15664360b4056a737bc5048ae8386.png" style="width:auto;"  loading="lazy">
    </picture>




                </a>
        </div>

        <div         class="title"
        style="color: #009cde;"
>
                <a         class="font-size1 font-weight-standard googlelinktracking"
        data-category="Cybersecurity"
        data-enable-google-event-tracking="True"
        data-label="HardeningGuide"
    target="_blank"
                href="https://doc.milestonesys.com/2020r1/en-US/portal/htm/chapter-page-hardening-guide.htm?tocpath=Tools &amp; Architecture|XProtect VMS hardening guide|_____0"
>
                    


    <span         class="textblock  font-weight-standard font-size1 textaligncenter"
        style="color: #009cde;"
>Guía de referencia Milestone </span>

                </a>
        </div>





            </div>

</div></div></div>


            </div>
        </div>
    </div>
</div><div class="tile custom-background-color no-margin-bottom col-xs-12 col-12" style="background-color: #efefef;">



    <div         class="container"
>
        <div class="row">
            <div         class="col-xs-12 col-12"
>
                







        <div class="title textaligncenter">
            


    <span         class="textblock  font-weight-light font-size10 textaligncenter"
><br />¿Es tu instalación cibersegura?</span>

        </div>



        <div class="title textaligncenter">
            


    <span         class="textblock  font-weight-standard font-size5 textaligncenter"
><br/>Haz nuestro curso online y aprende a identificar las diferentes amenazas de seguridad cibernéticas.<br/>  <br/></span>

        </div>









    <div         class="contentarea textaligncenter"
><div class="row"><div class="mediatile col-xs-12 col-12 col-sm-3">











    <div id="mediatileblock110291" class="mediatileblock textaligncenter">

        <div class="thumb"  >
    <picture>
        <!-- Use HTML conditional comments, to check the browser - https://scottjehl.github.io/picturefill/examples/demo-02.html -->
        <!--[if IE 9]><video style="display: none;"><![endif]-->
        <source srcset="" media="(max-width: 576px)">
        <!--[if IE 9]></video><![endif]-->

        <img src="https://mswebappcdn.azureedge.net/episerverprod/c8cf51fe54754d09817207db23625118/65cdffb13ca445babf46e45dd6fe14c3.png" style="width:auto;" alt="Blue checkmark"  loading="lazy">
    </picture>



        </div>

        <div         class="title font-size4 font-weight-standard"
>



    <span         class="textblock  font-weight-standard font-size4 textaligncenter"
>Identificar amenazas<br />y vulnerabilidades potenciales</span>
        </div>





            </div>

</div><div class="mediatile col-xs-12 col-12 col-sm-3">











    <div id="mediatileblock110287" class="mediatileblock textaligncenter">

        <div class="thumb"  >
    <picture>
        <!-- Use HTML conditional comments, to check the browser - https://scottjehl.github.io/picturefill/examples/demo-02.html -->
        <!--[if IE 9]><video style="display: none;"><![endif]-->
        <source srcset="" media="(max-width: 576px)">
        <!--[if IE 9]></video><![endif]-->

        <img src="https://mswebappcdn.azureedge.net/episerverprod/c8cf51fe54754d09817207db23625118/65cdffb13ca445babf46e45dd6fe14c3.png" style="width:auto;" alt="Blue checkmark"  loading="lazy">
    </picture>



        </div>

        <div         class="title font-size4 font-weight-standard"
>



    <span         class="textblock  font-weight-standard font-size4 textaligncenter"
>Aplicar medidas de seguridad<br/></span>
        </div>





            </div>

</div><div class="mediatile col-xs-12 col-12 col-sm-3">











    <div id="mediatileblock110288" class="mediatileblock textaligncenter">

        <div class="thumb"  >
    <picture>
        <!-- Use HTML conditional comments, to check the browser - https://scottjehl.github.io/picturefill/examples/demo-02.html -->
        <!--[if IE 9]><video style="display: none;"><![endif]-->
        <source srcset="" media="(max-width: 576px)">
        <!--[if IE 9]></video><![endif]-->

        <img src="https://mswebappcdn.azureedge.net/episerverprod/c8cf51fe54754d09817207db23625118/65cdffb13ca445babf46e45dd6fe14c3.png" style="width:auto;" alt="Blue checkmark"  loading="lazy">
    </picture>



        </div>

        <div         class="title font-size4 font-weight-standard"
>



    <span         class="textblock  font-weight-standard font-size4 textaligncenter"
>Configurar un sistema seguro<br/></span>
        </div>





            </div>

</div><div class="mediatile col-xs-12 col-12 col-sm-3">











    <div id="mediatileblock162888" class="mediatileblock textaligncenter">

        <div class="thumb"  >
    <picture>
        <!-- Use HTML conditional comments, to check the browser - https://scottjehl.github.io/picturefill/examples/demo-02.html -->
        <!--[if IE 9]><video style="display: none;"><![endif]-->
        <source srcset="" media="(max-width: 576px)">
        <!--[if IE 9]></video><![endif]-->

        <img src="https://mswebappcdn.azureedge.net/episerverprod/c8cf51fe54754d09817207db23625118/65cdffb13ca445babf46e45dd6fe14c3.png" style="width:auto;" alt="Blue checkmark"  loading="lazy">
    </picture>



        </div>

        <div         class="title font-size4 font-weight-standard"
>



    <span         class="textblock  font-weight-standard font-size4 textaligncenter"
>Aplicar cifrado<br/></span>
        </div>





            </div>

</div></div></div>

    <div         class="links textaligncenter"
>



<div class="buttonblock textaligncenter">
        <a target="_blank" href="https://go.bluevolt.com/Milestone/s/trainingtrackdetail/5143" data-category="Cybersecurity" data-label="Learning_and_Performance_es" data-enable-google-event-tracking="True" class="button hover background-color18 border-color18 googlelinktracking">
            

<span data-text-color="text-color13" data-background-color="background-color18" data-border-color="border-color18" data-hover-text-color="text-color13" data-hover-background-color="background-color38" data-hover-border-color="border-color38" data-active-text-color="text-color13" data-active-background-color="background-color37" data-active-border-color="border-color37" class="text-color13">Start learning</span>
        </a>
    </div>
    </div>

            </div>
        </div>
    </div>
</div></div>
  
    
    

    
    
    <div class="row"><div class="footer-column col-12 col-xs-12">
<div class="container">
    <div class="row footer-column__row-wrap">
        <div class="col-6 col-xs-6 col-sm-4 col-md-3">
            <ul class="footer-column__links-list footer-column__links-list--with-heading">
                <li class="footer-column__links-list-item">
                    <a class="footer-column__links-list-item-link" href="/solutions/platform/product-index/">Productos</a>
                </li>
                <li class="footer-column__links-list-item">
                    <a class="footer-column__links-list-item-link" href="/solutions/platform/video-management-software/">Software de gesti&#243;n de v&#237;deo XProtect&#174;</a>
                </li>
                <li class="footer-column__links-list-item">
                    <a class="footer-column__links-list-item-link" target="_blank" href="/es/campaigns/book-a-demo/">Reservar una demostraci&#243;n gratuita de VMS</a>
                </li>
                <li class="footer-column__links-list-item">
                    <a class="footer-column__links-list-item-link" href="/solutions/hardware-and-add-ons/milestone-addons/">Productos add-on XProtect&#174;</a>
                </li>
                <li class="footer-column__links-list-item">
                    <a class="footer-column__links-list-item-link" href="/solutions/hardware-and-add-ons/network-video-recorders/">Grabadores de v&#237;deo en red Husky™</a>
                </li>
                <li class="footer-column__links-list-item">
                    <a class="footer-column__links-list-item-link" href="/es/solutions/services/milestone-care/">Milestone Care™</a>
                </li>
            </ul>
        </div>

        <div class="col-6 col-xs-6 col-sm-4 col-md-3">
            <ul class="footer-column__links-list footer-column__links-list--with-heading">
                    <li class="footer-column__links-list-item">
                        <a class="footer-column__links-list-item-link" href="/community/find-a-milestone-partner/">D&#211;NDE COMPRARLO</a>
                    </li>
                    <li class="footer-column__links-list-item">
                        <a class="footer-column__links-list-item-link" href="/community/find-a-milestone-partner/resellers/">Encuentre un revendedor</a>
                    </li>
                    <li class="footer-column__links-list-item">
                        <a class="footer-column__links-list-item-link" href="/community/find-a-milestone-partner/distributors/">Encuentre un distribuidor</a>
                    </li>
            </ul>
        </div>

        <div class="col-6 col-xs-6 col-sm-4 col-md-3">
            <ul class="footer-column__links-list footer-column__links-list--with-heading">
                    <li class="footer-column__links-list-item">
                        <a class="footer-column__links-list-item-link" href="/es/support/">Asistencia</a>
                    </li>
                    <li class="footer-column__links-list-item">
                        <a class="footer-column__links-list-item-link" href="/community/business-partner-tools/supported-devices/">Dispositivos compatibles</a>
                    </li>
                    <li class="footer-column__links-list-item">
                        <a class="footer-column__links-list-item-link" href="https://supportcommunity.milestonesys.com/s/my-cases">Asistencia para socios</a>
                    </li>
                    <li class="footer-column__links-list-item">
                        <a class="footer-column__links-list-item-link" href="/support/resources/download-software/">Descargar software</a>
                    </li>
            </ul>
        </div>

        <div class="col-6 col-xs-6 col-sm-4 col-md-3">
            <ul class="footer-column__links-list footer-column__links-list--with-heading">
                    <li class="footer-column__links-list-item">    
                        <a class="footer-column__links-list-item-link" target="_blank" href="/es/comunidad/marketplace/start-exploring/">MARKETPLACE</a>
                    </li>
                    <li class="footer-column__links-list-item">    
                        <a class="footer-column__links-list-item-link" target="_blank" href="/es/comunidad/marketplace/start-exploring/">Empiece a descubrir</a>
                    </li>
                    <li class="footer-column__links-list-item">    
                        <a class="footer-column__links-list-item-link" target="_blank" href="/es/under-construction/lavinia/what-is-marketplace/">&#191;En qu&#233; consiste Marketplace?</a>
                    </li>
                    <li class="footer-column__links-list-item">    
                        <a class="footer-column__links-list-item-link" target="_blank" href="/es/under-construction/lavinia/join-marketplace/">&#218;nase a Marketplace</a>
                    </li>
                    <li class="footer-column__links-list-item">    
                        <a class="footer-column__links-list-item-link" target="_blank" href="/es/my-milestone/marketplace/">Iniciar sesi&#243;n en Marketplace</a>
                    </li>
                    <li class="footer-column__links-list-item">    
                        <a class="footer-column__links-list-item-link" target="_blank" href="/es/comunidad/marketplace/support/">Asistencia de Marketplace</a>
                    </li>
            </ul>
        </div>

        <div class="col-6 col-xs-6 col-sm-4 col-md-3">
            <ul class="footer-column__links-list footer-column__links-list--with-heading">
                    <li class="footer-column__links-list-item">
                        <a class="footer-column__links-list-item-link" href="/events/">Eventos</a>
                    </li>
                    <li class="footer-column__links-list-item">
                        <a class="footer-column__links-list-item-link" href="/es/events/?nogeo=1">Pr&#243;ximos eventos</a>
                    </li>
                    <li class="footer-column__links-list-item">
                        <a class="footer-column__links-list-item-link" href="/es/events/?ct=webinar">Seminarios en l&#237;nea</a>
                    </li>
                    <li class="footer-column__links-list-item">
                        <a class="footer-column__links-list-item-link" href="/events/webinars/recorded-webinars/">Seminarios en l&#237;nea grabados</a>
                    </li>
            </ul>
        </div>


        <div class="col-6 col-xs-6 col-sm-4 col-md-3">
            <ul class="footer-column__links-list footer-column__links-list--with-heading">
          
                    <li class="footer-column__links-list-item">
                        <a class="footer-column__links-list-item-link" href="/es/comunidad/hagase-socio/">Socios</a>
                    </li>
                    <li class="footer-column__links-list-item">
                        <a class="footer-column__links-list-item-link" href="/my-milestone/">My Milestone</a>
                    </li>
                    <li class="footer-column__links-list-item">
                        <a class="footer-column__links-list-item-link" href="/community/become-a-partner/the-open-platform/">Plataforma abierta</a>
                    </li>
                    <li class="footer-column__links-list-item">
                        <a class="footer-column__links-list-item-link" href="/community/become-a-partner/">Convi&#233;rtase en socio</a>
                    </li>
                    <li class="footer-column__links-list-item">
                        <a class="footer-column__links-list-item-link" href="/es/solutions/services/learning-and-performance/">Portal informativo</a>
                    </li>

            </ul>
        </div>
         <div class="col-6 col-xs-6 col-sm-4 col-md-3">
                <ul class="footer-column__links-list footer-column__links-list--with-heading footer-column__links-list">
                    <li class="footer-column__links-list-item">FOLLOW US</li>
                    <li class="footer-column__links-list-item footer-column__links-list-item--no-opacity footer-column__links-list-item--align-row">
                        <div><div>
<a class="footer-column__links-list-item-link"  data-label="FollowUS_Linkedin_es" data-category="Footer" target="_blank" href="https://www.linkedin.com/company/milestone-systems"> 
    <svg class="msds-icon">
        <use href="/Static/dist/msds-spritemap.svg#linkedin"></use>
    </svg>
</a>
  
         
</div><div>
<a class="footer-column__links-list-item-link"  data-label="FollowUS_Facebook_es" data-category="Footer" target="_blank" href="https://www.facebook.com/milestonesys"> 
    <svg class="msds-icon">
        <use href="/Static/dist/msds-spritemap.svg#social-facebook"></use>
    </svg>
</a>
  
         
</div><div>
<a class="footer-column__links-list-item-link"  data-label="FollowUS_Twitter_es" data-category="Footer" target="_blank" href="https://twitter.com/milestonesys"> 
    <svg class="msds-icon">
        <use href="/Static/dist/msds-spritemap.svg#social-twitter"></use>
    </svg>
</a>
  
         
</div><div>
<a class="footer-column__links-list-item-link"  data-label="FollowUS_Instagram_es" data-category="Footer" target="_blank" href="https://www.instagram.com/milestonesystems/"> 
    <svg class="msds-icon">
        <use href="/Static/dist/msds-spritemap.svg#social-instagram"></use>
    </svg>
</a>
  
         
</div><div>
<a class="footer-column__links-list-item-link"  data-label="FollowUS_Youtube_es" data-category="Footer" target="_blank" href="https://www.youtube.com/user/Milestonesys"> 
    <svg class="msds-icon">
        <use href="/Static/dist/msds-spritemap.svg#social-youtube"></use>
    </svg>
</a>
  
         
</div></div>
                    </li>
                   

                </ul>
        </div>


        <div class="col-md-3 col-6 col-xs-6">
            <div class="footer-column__icon">
                <?xml version="1.0" encoding="UTF-8" ?>
                <svg width="101px" height="30px" viewBox="0 0 101 30" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                    <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                        <g id="Footer" transform="translate(-1020.000000, -303.000000)">
                            <g id="Component-/-Footer-/-Desktop">
                                <g id="Footer/New">
                                    <g id="Group-3" transform="translate(150.000000, 72.000000)">
                                        <g id="Graphic-elements-/-Branding-/-02-Dark-theme-/-Payoff--/-White" transform="translate(870.000000, 231.000000)">
                                            <g id="Group">
                                                <polygon id="Fill-43" fill="#FFFFFF" points="93.7797596 17.6897394 100.654773 17.6549568 100.664593 19.5707829 96.1041623 19.5930437 96.1181901 22.3659133 100.312495 22.3450437 100.322315 24.2107828 96.1280095 24.2316524 96.1448429 27.270261 100.75437 27.2452176 100.76419 29.1777393 93.8400791 29.2125219"></polygon>
                                                <polygon id="Fill-40" fill="#FFFFFF" points="84.6541337 17.7373214 91.5291473 17.7025388 91.5389667 19.6183649 86.9785363 19.6406257 86.9925641 22.4134953 91.1868695 22.3926257 91.1966889 24.2583648 87.0023836 24.2792344 87.0192169 27.3164517 91.6287445 27.2927995 91.6385639 29.2239299 84.7144531 29.2601039"></polygon>
                                                <path d="M81.9692143,19.8486265 C81.0517976,19.4896699 80.3181449,19.3602786 79.6027282,19.3644525 C78.3710894,19.371409 77.5911449,19.887583 77.5953533,20.6806265 C77.5995616,21.3888004 77.9839227,21.8340178 79.7023255,22.4350613 C81.8696171,23.1821918 82.7912421,24.1686266 82.7996587,25.8701918 C82.8122837,28.0823658 81.1205338,29.4778441 78.4412283,29.4917572 C77.3260199,29.4973224 76.3258394,29.3359311 75.3593255,29.0131484 L75.5641311,26.981844 C76.5657144,27.4548875 77.4817283,27.6315832 78.2981449,27.6274093 C79.5297838,27.6204528 80.4093254,27.1042788 80.4051171,26.1804527 C80.399506,25.3053223 79.9141449,24.8461918 78.1466449,24.2103657 C76.0789505,23.4771483 75.1909922,22.5574961 75.1825755,20.9227134 C75.1727561,18.877496 76.8462699,17.579409 79.3277838,17.565496 C80.3588254,17.5599307 81.2257421,17.6740177 82.141756,17.9648003 L81.9692143,19.8486265 Z" id="Fill-37" fill="#FFFFFF"></path>
                                                <path d="M62.0727776,27.612244 L62.6885971,27.6094614 C65.2683054,27.5955483 67.3275831,26.5771135 67.3121525,23.621983 C67.2953192,20.517983 65.226222,19.6539829 62.6465137,19.667896 L62.0306943,19.6706786 L62.0727776,27.612244 Z M62.8541249,17.8508524 C66.7819027,17.8299829 69.7207222,19.3673743 69.7431667,23.6261571 C69.7642083,27.6539834 66.7594583,29.3541574 62.9158471,29.3736356 L59.7357498,29.3903313 L59.6754304,17.8675481 L62.8541249,17.8508524 Z" id="Fill-34" fill="#FFFFFF"></path>
                                                <polygon id="Fill-31" fill="#FFFFFF" points="51.3498039 17.9112354 53.696651 17.8973223 53.747151 27.4402784 58.2570814 27.4180175 58.2683036 29.3978435 51.4101233 29.4326261"></polygon>
                                                <path d="M43.4311214,22.9043474 L44.1128714,22.9001735 C45.9617325,22.8918257 46.7893713,22.4243474 46.7837602,21.2695648 C46.7767463,20.013217 45.7779686,19.7558257 44.0960381,19.7641735 L43.4142881,19.7683474 L43.4311214,22.9043474 Z M41.0576214,17.9638257 L44.4200797,17.94713 C47.2831492,17.9318257 49.183913,18.5328692 49.196538,20.9439995 C49.2049547,22.4619125 48.2945519,23.3746081 46.7809547,23.680695 L46.7809547,23.712695 C47.5973714,23.922782 47.9003714,24.3833037 48.2707047,25.2403472 L50.0901075,29.4406948 L47.5103992,29.4532166 L46.1959964,26.190608 C45.7050242,24.9899124 45.4875936,24.6754776 44.0567603,24.6838254 L43.4409409,24.6866081 L43.4661909,29.4754774 L41.1179409,29.4866079 L41.0576214,17.9638257 Z" id="Fill-28" fill="#FFFFFF"></path>
                                                <path d="M30.2294396,23.7984002 C30.2420646,26.3083133 31.5157868,27.9361394 33.4474117,27.9264003 C35.29487,27.9166611 36.5840228,26.224835 36.5713978,23.7483132 C36.55737,21.1730088 35.2850506,19.5952696 33.3379951,19.6050088 C31.4723007,19.6147479 30.2168146,21.274574 30.2294396,23.7984002 M39.0683423,23.6870954 C39.0865784,27.3684865 36.8533562,29.7086603 33.3913007,29.7253559 C29.961509,29.7434429 27.7353007,27.4603126 27.7170646,23.8109214 C27.6960229,19.9987477 29.8156201,17.8241392 33.4600368,17.8046609 C36.8729951,17.7865739 39.0487034,20.0377043 39.0683423,23.6870954" id="Fill-25" fill="#FFFFFF"></path>
                                                <path d="M19.1099015,21.8921732 C18.9906653,21.3648689 18.7521931,20.3575646 18.6652209,19.7314777 L18.632957,19.7314777 C18.5515959,20.3589559 18.3748459,21.3495645 18.2612209,21.8963471 L16.5708737,29.613912 L13.6082071,29.6306076 L10.3341239,18.1231299 L12.8479016,18.1106082 L14.5649016,25.0017383 C14.650471,25.3815643 15.0250127,27.0469556 15.1288182,27.8233033 L15.1624849,27.8233033 C15.2761099,27.0455643 15.6001515,25.3773904 15.6801099,24.9947817 L17.1586376,18.0883473 L20.2714014,18.0716517 L21.9056375,24.9641731 C22.0080403,25.3606948 22.3334847,27.0246947 22.4541236,27.7829555 L22.4863875,27.7829555 C22.5986097,27.0233034 22.9240542,25.3885209 23.0208458,24.9586078 L24.6494708,18.0493908 L26.9794846,18.036869 L23.928443,29.5749554 L20.981207,29.5916511 L19.1099015,21.8921732 Z" id="Fill-22" fill="#FFFFFF"></path>
                                                <polygon id="Fill-19" fill="#FFFFFF" points="83.6198659 0.0361739119 90.4948795 4.73695157e-15 90.5046989 1.91582602 85.9442686 1.9394782 85.9582963 4.71234767 90.1526017 4.6900868 90.1624212 6.55582587 85.9681158 6.57808674 85.9849491 9.61530404 90.5944767 9.59165186 90.6042961 11.5227822 83.6801853 11.5589561"></polygon>
                                                <polygon id="Fill-16" fill="#FFFFFF" points="71.6613257 0.0986434822 74.026409 0.0847304382 74.0502563 4.67603498 78.710284 4.64960019 78.685034 0.0624695677 81.033284 0.0499478281 81.0936034 11.5727309 78.7467562 11.5852527 78.7201034 6.60020897 74.0600757 6.62246984 74.0867285 11.6075135 71.7216452 11.6200353"></polygon>
                                                <polygon id="Fill-13" fill="#FFFFFF" points="70.2050989 2.05384356 66.9590713 2.02045225 67.0095713 11.6468874 64.6290575 11.6594092 64.5785575 2.03297399 61.3998631 2.0997566 61.3900437 0.151930436 70.1952795 0.106017391"></polygon>
                                                <polygon id="Fill-10" fill="#FFFFFF" points="49.3251753 0.214121731 56.2001889 0.177947819 56.2100084 2.09377384 51.649578 2.11742602 51.6636058 4.89029549 55.8579112 4.86803462 55.8677306 6.735165 51.6734252 6.75603456 51.6902586 9.79325185 56.2997861 9.76959968 56.3096056 11.7007301 49.3854948 11.736904"></polygon>
                                                <path d="M40.5255486,11.7835131 L38.1787014,11.7960348 L38.1169792,0.273252171 L40.4652292,0.260730432 L40.4918819,5.27777393 L40.5241458,5.27777393 C40.9870625,4.68090437 42.0784236,3.32299132 42.5245069,2.79290436 L44.6932014,0.238469562 L47.6053681,0.223165214 L42.7237014,5.62977393 L48.1328125,11.7445566 L44.9695486,11.7598609 L42.3898403,8.66977395 C41.9535764,8.16055656 41.1497847,7.10733916 40.5297569,6.23499133 L40.4960903,6.23638263 L40.5255486,11.7835131 Z" id="Fill-7" fill="#FFFFFF"></path>
                                                <path d="M31.5643235,4.73043475 C31.3104207,4.03895648 30.9036151,2.71999995 30.7521151,2.12591298 L30.7184485,2.12591298 C30.5543234,2.72139125 30.1292818,4.0445217 29.8823929,4.73878258 L28.9313095,7.43513044 L32.5434624,7.41704348 L31.5643235,4.73043475 Z M36.7616153,11.8024353 L34.2155736,11.8163483 L33.1859347,9.16452211 L28.342143,9.18817428 L27.3405597,11.8525222 L24.9263791,11.865044 L29.4264902,0.317217398 L32.0735319,0.303304354 L36.7616153,11.8024353 Z" id="Fill-4" fill="#FFFFFF"></path>
                                                <path d="M15.9460759,5.88535646 C16.267312,6.84118253 16.6741176,8.22692165 16.9462565,9.29683468 L16.9785204,9.29683468 C17.289937,8.22413904 17.6827148,6.83422601 17.9927287,5.87283472 L19.8289647,0.367443488 L23.4733813,0.349356532 L23.5351035,11.872139 L21.2878536,11.8832694 L21.2583953,6.25405211 C21.2527841,5.13266082 21.2583953,3.34900867 21.285048,2.02726955 L21.2527841,2.02726955 C20.9245341,3.1333565 20.4012981,4.78900865 20.1389786,5.63213907 L17.9253953,11.8999651 L15.8282426,11.9124868 L13.6314927,5.73231298 C13.446326,5.22031299 12.7351177,2.97892172 12.4798121,2.0731826 L12.4461455,2.0731826 C12.486826,3.39353041 12.5134788,5.17579125 12.5190899,6.29996515 L12.5485483,11.9291825 L10.4008955,11.9403129 L10.3405761,0.41613914 L14.102826,0.398052184 L15.9460759,5.88535646 Z" id="Fill-1" fill="#FFFFFF"></path>
                                                <polygon id="Yellow-bar" fill="#FFE700" points="1.86148612 29.6761042 0.154305556 29.6858433 -1.14345274e-12 0.454539137 1.70718057 0.446191311"></polygon>
                                            </g>
                                        </g>
                                    </g>
                                </g>
                            </g>
                        </g>
                    </g>
                </svg>
            </div>

        </div>

    </div> <!-- ROW END -->

    <div class="row">
        <div class="col-md-12 footer-column__breaker-wrapper">
            <div class="footer-column__breaker-wrapper-breaker"></div>
        </div>
        <div class="col-6 col-xs-6 col-sm-3 col-md-3">

            <ul class="footer-column__links-list">
                <li class="footer-column__links-list-item">
                    <a class="footer-column__links-list-item-link" target="_blank" href="/es/about-us/Localizaciones/">Ll&#225;menos</a>
                </li>
                <li class="footer-column__links-list-item">
                    <a class="footer-column__links-list-item-link" href="/es/contact-milestone/">P&#243;ngase en contacto con nosotros</a>
                </li>
                <li class="footer-column__links-list-item">
                    <a class="footer-column__links-list-item-link" href="/es/about-us/career/">Carreras profesionales</a>
                </li>
                <li class="footer-column__links-list-item">
                    <a class="footer-column__links-list-item-link" href="https://pardot.milestonesys.com/marketing-communication">Reg&#237;strese para recibir las noticias</a>
                </li>
                <li class="footer-column__links-list-item">
                    <a class="footer-column__links-list-item-link" href="/terms-of-use/">T&#233;rminos de uso</a>
                </li>
            </ul>
        </div>

        <div class="col-6 col-xs-6 col-sm-3 col-md-3">
            <ul class="footer-column__links-list">
                <li class="footer-column__links-list-item">
                    <a class="footer-column__links-list-item-link" href="/es/privacy-policy/">Pol&#237;tica de privacidad</a>
                </li>
                <li class="footer-column__links-list-item">
                    <a class="footer-column__links-list-item-link" href="/es/cookie-policy-milestone-systems/">Pol&#237;tica de cookies</a>
                </li>
                <li class="footer-column__links-list-item">
                    <a class="footer-column__links-list-item-link" href="/es/politica-de-precio-minimo-anunciado/">Pol&#237;tica de MAP</a>
                </li>
                <li class="footer-column__links-list-item">
                    <a class="footer-column__links-list-item-link" target="_blank" href="/es/content-hub/covid-19-milestone-announcement/">Declaraci&#243;n sobre COVID-19</a>
                </li>
            </ul>
        </div>

        <div class="col-12 col-xs-12 col-md-3 offset-md-3 col-md-offset-3">
            <p class="footer-column__text">
                Para cualquier asunto relacionado con el cumplimiento, puede enviarnos un correo electrónico a compliance@milestonesys.com<br /><br />Copyright © [#AÑO] Milestone Systems A/S. Todos los derechos reservados.
            </p>
        </div>
    </div><!-- ROW END -->
</div>


</div></div> 	
    
</div>


    <script>
                function loadApplicationInsights() {
            var appInsights = window.appInsights || function (config) {
                    function i(config) { t[config] = function () { var i = arguments; t.queue.push(function () { t[config].apply(t, i) }) } } var t = { config: config }, u = document, e = window, o = "script", s = "AuthenticatedUserContext", h = "start", c = "stop", l = "Track", a = l + "Event", v = l + "Page", y = u.createElement(o), r, f; y.src = config.url || "https://az416426.vo.msecnd.net/scripts/a/ai.0.js"; u.getElementsByTagName(o)[0].parentNode.appendChild(y); try { t.cookie = u.cookie } catch (p) { } for (t.queue = [], t.version = "1.0", r = ["Event", "Exception", "Metric", "PageView", "Trace", "Dependency"]; r.length;) i("track" + r.pop()); return i("set" + s), i("clear" + s), i(h + a), i(c + a), i(h + v), i(c + v), i("flush"), config.disableExceptionTracking || (r = "onerror", i("_" + r), f = e[r], e[r] = function (config, i, u, e, o) { var s = f && f(config, i, u, e, o); return s !== !0 && t["_" + r](config, i, u, e, o), s }), t
                }({
                    instrumentationKey: "423b0e98-6181-420e-9f29-15b56c2f8683"
                });

            window.appInsights = appInsights;
            appInsights.trackPageView();
        }

        function loadPardot() {
            piAId = '54942';
            piCId = '2432';

            (function async_load() {
                var s = document.createElement('script');
                s.type = 'text/javascript';
                s.src = ('https:' == document.location.protocol ? 'https://pi' : 'http://cdn') + '.pardot.com/pd.js';
                var c = document.getElementsByTagName('script')[0];
                c.parentNode.insertBefore(s, c);
            })();
        }

        function loadCookiebotDependedScripts() {
            window.addEventListener('CookiebotOnAccept', function (e) {
                if (Cookiebot.consent.statistics) {
                    loadApplicationInsights();
                }

                if (Cookiebot.consent.marketing) {
                    loadPardot();
                }
            }, false);
        }

        if (window.location.href.includes('local.milestone.dk')) {
            loadApplicationInsights()
            loadPardot()
        }
        else {
            var cookiebotScript = document.querySelector("#Cookiebot")
            cookiebotScript.onload = loadCookiebotDependedScripts
            cookiebotScript.src = "https://consent.cookiebot.com/uc.js"
        }

        //Measures TTI
        window.addEventListener('load', function () {
            if (window.performance) {
                const resources = window.performance.getEntriesByType("resource")
                    .filter(resource => (resource.name.includes("//www.milestonesys.com")
                        || resource.name.includes("//www.milestonesys.qa")
                        || resource.name.includes("//www.milestonesys.wtst")
                        || resource.name.includes("//www.milestonesys.wdev")
                        || resource.name.includes("//local.milestone.dk")
                        || resource.name.includes("opensans")
                        || resource.name.includes("//mswebappcdn.azureedge.net"))
                        && !resource.name.includes("favicon.ico"))
                    .sort((a, b) => b.responseEnd - a.responseEnd)
                const loadTime = resources[0].responseEnd

                console.log(`TTI: ${loadTime / 1000} s, resource number: ${resources.length}`)

                const ttiElement = document.createElement('div')
                ttiElement.hidden = true
                ttiElement.id = 'tti'
                ttiElement.innerText = loadTime
                document.body.appendChild(ttiElement)
            }
        })
    </script>
</body>
</html>"

    
@app.route('/lenguajes')
def mostrarLenguajes():
    misLenguajes = ("PHP", "Python", "Java", "C#",
                    "JavaScript", "Perl", "Ruby", "Rust")
    return render_template('lenguajes.html', lenguajes=misLenguajes)


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route("/get-price/<ticker>")
def get_price(ticker):
    url = f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{ticker}?modules=price%2CsummaryDetail%2CpageViews%2CfinancialsTemplate"
    headers={'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url,headers=headers)
    company_info = response.json()

    if response.status_code > 400:
        app.logger.info(f"Yahoo has problem with ticker: {ticker}.")
        app.logger.info(f"Yahoo status code: {response.status_code}.")
        return Response({}, status=404, mimetype='application/json')

    app.logger.info(company_info)

    try:
        price = company_info['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
        company_name = company_info['quoteSummary']['result'][0]['price']['longName']
        exchange = company_info['quoteSummary']['result'][0]['price']['exchangeName']
        currency = company_info['quoteSummary']['result'][0]['price']['currency']

        result = {
            "price": price,
            "name": company_name,
            "exchange": exchange,
            "currency": currency
        }
        app.logger.info(result)

        return Response(json.dumps(result), status=200, mimetype='application/json')
    except (KeyError, TypeError):
        return Response({}, status=404, mimetype='application/json')
    except Exception as e:
        app.logger.error("Exception occurred", exc_info=True)


if __name__ == '__main__':
    app.run()



