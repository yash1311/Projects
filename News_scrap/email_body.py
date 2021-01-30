


def email_html(df):

    head_html = """
        <html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">
        <head>
        <!--[if gte mso 9]><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
        <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
        <meta content="width=device-width" name="viewport"/>
        <!--[if !mso]><!-->
        <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
        <!--<![endif]-->
        <title></title>
        <!--[if !mso]><!-->
        <!--<![endif]-->
        <style type="text/css">
                body {
                    margin: 0;
                    padding: 0;
                }
    
                table,
                td,
                tr {
                    vertical-align: top;
                    border-collapse: collapse;
                }
    
                * {
                    line-height: inherit;
                }
    
                a[x-apple-data-detectors=true] {
                    color: inherit !important;
                    text-decoration: none !important;
                }
            </style>
        <style id="media-query" type="text/css">
                @media (max-width: 520px) {
    
                    .block-grid,
                    .col {
                        min-width: 320px !important;
                        max-width: 100% !important;
                        display: block !important;
                    }
    
                    .block-grid {
                        width: 100% !important;
                    }
    
                    .col {
                        width: 100% !important;
                    }
    
                    .col_cont {
                        margin: 0 auto;
                    }
    
                    img.fullwidth,
                    img.fullwidthOnMobile {
                        max-width: 100% !important;
                    }
    
                    .no-stack .col {
                        min-width: 0 !important;
                        display: table-cell !important;
                    }
    
                    .no-stack.two-up .col {
                        width: 50% !important;
                    }
    
                    .no-stack .col.num2 {
                        width: 16.6% !important;
                    }
    
                    .no-stack .col.num3 {
                        width: 25% !important;
                    }
    
                    .no-stack .col.num4 {
                        width: 33% !important;
                    }
    
                    .no-stack .col.num5 {
                        width: 41.6% !important;
                    }
    
                    .no-stack .col.num6 {
                        width: 50% !important;
                    }
    
                    .no-stack .col.num7 {
                        width: 58.3% !important;
                    }
    
                    .no-stack .col.num8 {
                        width: 66.6% !important;
                    }
    
                    .no-stack .col.num9 {
                        width: 75% !important;
                    }
    
                    .no-stack .col.num10 {
                        width: 83.3% !important;
                    }
    
                    .video-block {
                        max-width: none !important;
                    }
    
                    .mobile_hide {
                        min-height: 0px;
                        max-height: 0px;
                        max-width: 0px;
                        display: none;
                        overflow: hidden;
                        font-size: 0px;
                    }
    
                    .desktop_hide {
                        display: block !important;
                        max-height: none !important;
                    }
                }
            </style>
        <style id="icon-media-query" type="text/css">
                @media (max-width: 520px) {
                    .icons-inner {
                        text-align: center;
                    }
    
                    .icons-inner td {
                        margin: 0 auto;
                    }
                }
            </style>
        </head>
        <body class="clean-body" style="margin: 0; padding: 0; -webkit-text-size-adjust: 100%; background-color: #FFFFFF;">
        <!--[if IE]><div class="ie-browser"><![endif]-->
        <table bgcolor="#FFFFFF" cellpadding="0" cellspacing="0" class="nl-container" role="presentation" style="table-layout: fixed; vertical-align: top; min-width: 320px; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #FFFFFF; width: 100%;" valign="top" width="100%">
        <tbody>
        <tr style="vertical-align: top;" valign="top">
        <td style="word-break: break-word; vertical-align: top;" valign="top">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color:#FFFFFF"><![endif]-->
        <div style="background-color:transparent;">
        <div class="block-grid" style="min-width: 320px; max-width: 500px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: transparent;">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:500px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
        <!--[if (mso)|(IE)]><td align="center" width="500" style="background-color:transparent;width:500px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
        <div class="col num12" style="min-width: 320px; max-width: 500px; display: table-cell; vertical-align: top; width: 500px;">
        <div class="col_cont" style="width:100% !important;">
        <!--[if (!mso)&(!IE)]><!-->
        <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
        <!--<![endif]-->
        <table cellpadding="0" cellspacing="0" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" valign="top" width="100%">
        <tr style="vertical-align: top;" valign="top">
        <td align="center" style="word-break: break-word; vertical-align: top; padding-bottom: 0px; padding-left: 0px; padding-right: 0px; padding-top: 0px; text-align: center; width: 100%;" valign="top" width="100%">
        <h1 style="color:#555555;direction:ltr;font-family:Arial, Helvetica Neue, Helvetica, sans-serif;font-size:23px;font-weight:normal;line-height:120%;text-align:center;margin-top:0;margin-bottom:0;">All about reliance for the day..!!</h1>
        </td>
        </tr>
        </table>
        """

    body_html = ""

    for i in range(len(df.index)):
        title = df.loc[i]['title']
        url = df.loc[i]['url']
        # imgurl=df.loc[i]['urlToImage']
        publishedAt = df.loc[i]['publishedAt']
        source = df.loc[i]['source'].get('name')
        body_html = body_html + f"""<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]-->
                                                                <div style="color:#555555;font-family:Arial, Helvetica Neue, Helvetica, sans-serif;line-height:1.2;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
                                                                <div class="txtTinyMce-wrapper" style="line-height: 1.2; font-size: 12px; color: #555555; font-family: Arial, Helvetica Neue, Helvetica, sans-serif; mso-line-height-alt: 14px;">
                                                                <p style="line-height: 1.2; word-break: break-word; mso-line-height-alt: 14px; margin: 0;">{i + 1}. <a href="{url}" rel="noopener" style="text-decoration: underline; color: #0068A5;" target="_blank">{title}</a></p>
                                                                <p style="line-height: 1.2; word-break: break-word; mso-line-height-alt: 14px; margin: 0;">Published at: {publishedAt}               Published on: {source}</p>
                                                                </div>
                                                                </div>
                                                                """


    tail_html = """
                <!--[if mso]></td></tr></table><![endif]-->
                <!--[if (!mso)&(!IE)]><!-->
                </div>
                <!--<![endif]-->
                </div>
                </div>
                <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                </div>
                </div>
                </div>
                <div style="background-color:transparent;">
                <div class="block-grid" style="min-width: 320px; max-width: 500px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: transparent;">
                <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
                <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:500px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
                <!--[if (mso)|(IE)]><td align="center" width="500" style="background-color:transparent;width:500px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
                <div class="col num12" style="min-width: 320px; max-width: 500px; display: table-cell; vertical-align: top; width: 500px;">
                <div class="col_cont" style="width:100% !important;">
                <!--[if (!mso)&(!IE)]><!-->
                <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
                <!--<![endif]-->
                <table cellpadding="0" cellspacing="0" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" valign="top" width="100%">
                <tr style="vertical-align: top;" valign="top">
                <td align="center" style="word-break: break-word; vertical-align: top; padding-top: 5px; padding-right: 0px; padding-bottom: 5px; padding-left: 0px; text-align: center;" valign="top">
                <!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
                <!--[if !vml]><!-->
                <table cellpadding="0" cellspacing="0" class="icons-inner" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; margin-right: -4px; padding-left: 0px; padding-right: 0px;" valign="top">
                <!--<![endif]-->
                </tr>
                </table>
                </td>
                </tr>
                </table>
                <!--[if (!mso)&(!IE)]><!-->
                </div>
                <!--<![endif]-->
                </div>
                </div>
                <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
                </div>
                </div>
                </div>
                <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                </td>
                </tr>
                </tbody>
                </table>
                <!--[if (IE)]></div><![endif]-->
                </body>
                </html>
                """
    email_msg=head_html+body_html+tail_html

    return email_msg