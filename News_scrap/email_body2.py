


def email_html(df,topic):

    head_html = """"
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
            
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
            <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css?family=Droid+Serif" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css?family=Merriweather" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css?family=Poppins" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css?family=Questrial" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css?family=Permanent+Marker" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css?family=Shrikhand" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css?family=Oswald" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css?family=Abril+Fatface" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css?family=Oxygen" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css?family=Nunito" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css?family=Noto+Sans" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css?family=Fira+Sans" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css?family=Bitter" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css?family=Cabin" rel="stylesheet" type="text/css"/>
            <link href="https://fonts.googleapis.com/css?family=Playfair+Display" rel="stylesheet" type="text/css"/>
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
                    @media (max-width: 660px) {
            
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
                    @media (max-width: 660px) {
                        .icons-inner {
                            text-align: center;
                        }
            
                        .icons-inner td {
                            margin: 0 auto;
                        }
                    }
                </style>
            </head>
            <body class="clean-body" style="margin: 0; padding: 0; -webkit-text-size-adjust: 100%; background-color: #ffffff;">
            <!--[if IE]><div class="ie-browser"><![endif]-->
            <table bgcolor="#ffffff" cellpadding="0" cellspacing="0" class="nl-container" role="presentation" style="table-layout: fixed; vertical-align: top; min-width: 320px; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; width: 100%;" valign="top" width="100%">
            <tbody>
            <tr style="vertical-align: top;" valign="top">
            <td style="word-break: break-word; vertical-align: top;" valign="top">
            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color:#ffffff"><![endif]-->
            <div style="background-color:transparent;">
            <div class="block-grid" style="min-width: 320px; max-width: 640px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: #141039;">
            <div style="border-collapse: collapse;display: table;width: 100%;background-color:#141039;">
            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:640px"><tr class="layout-full-width" style="background-color:#141039"><![endif]-->
            <!--[if (mso)|(IE)]><td align="center" width="640" style="background-color:#141039;width:640px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 40px; padding-left: 40px; padding-top:35px; padding-bottom:35px;"><![endif]-->
            <div class="col num12" style="min-width: 320px; max-width: 640px; display: table-cell; vertical-align: top; width: 640px;">
            <div class="col_cont" style="width:100% !important;">
            <!--[if (!mso)&(!IE)]><!-->
            <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:35px; padding-bottom:35px; padding-right: 40px; padding-left: 40px;">
            <!--<![endif]-->
            <div align="center" class="img-container center autowidth" style="padding-right: 0px;padding-left: 0px;">
            <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" align="center"><![endif]--><img align="center" alt="Sponsored by ''RealityWings''" border="0" class="center autowidth" src="https://realitywings.com/wp-content/uploads/2020/03/290-a.png" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 290px; display: block;" title="Sponsored by ''RealityWings''" width="290"/>
            <div style="font-size:1px;line-height:10px"> </div>
            <!--[if mso]></td></tr></table><![endif]-->
            </div>
                """

    body_html = f"""
            <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top: 25px; padding-bottom: 0px; font-family: Arial, sans-serif"><![endif]-->
            <div style="color:#555555;font-family:'Poppins', Arial, Helvetica, sans-serif;line-height:1.2;padding-top:25px;padding-right:0px;padding-bottom:0px;padding-left:0px;">
            <div class="txtTinyMce-wrapper" style="line-height: 1.2; font-size: 12px; font-family: 'Poppins', Arial, Helvetica, sans-serif; color: #555555; mso-line-height-alt: 14px;">
            <p style="font-size: 14px; line-height: 1.2; word-break: break-word; font-family: Poppins, Arial, Helvetica, sans-serif; mso-line-height-alt: 17px; margin: 0;"><span style="color: #ed9090; font-size: 14px;"><strong><span style="">IT'S A all about</span></strong></span></p>
            </div>
            </div>
            <!--[if mso]></td></tr></table><![endif]-->
            <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top: 0px; padding-bottom: 0px; font-family: Georgia, serif"><![endif]-->
            <div style="color:#555555;font-family:'Playfair Display', Georgia, serif;line-height:1.2;padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;">
            <div class="txtTinyMce-wrapper" style="line-height: 1.2; font-size: 12px; font-family: 'Playfair Display', Georgia, serif; color: #555555; mso-line-height-alt: 14px;">
            <p style="line-height: 1.2; word-break: break-word; font-family: 'Playfair Display', Georgia, serif; font-size: 50px; mso-line-height-alt: 60px; margin: 0;"><span style="color: #f5a2a2; font-size: 50px;"><strong><span style=""><span style="">"{topic}" <span style="font-size: 30px;">for the day.</span></span></span></strong></span></p>
            </div>
            </div>
            <!--[if mso]></td></tr></table><![endif]-->
            <table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%">
            <tbody>
            <tr style="vertical-align: top;" valign="top">
            <td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 5px; padding-bottom: 10px; padding-left: 0px;" valign="top">
            <table align="left" border="0" cellpadding="0" cellspacing="0" class="divider_content" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 5px solid #75997E; width: 35%;" valign="top" width="35%">
            <tbody>
            <tr style="vertical-align: top;" valign="top">
            <td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top"><span></span></td>
            </tr>
            </tbody>
            </table>
            </td>
            </tr>
            </tbody>
            </table>
            <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top: 30px; padding-bottom: 25px; font-family: Arial, sans-serif"><![endif]-->
            <div style="color:#ffffff;font-family:'Poppins', Arial, Helvetica, sans-serif;line-height:1.5;padding-top:30px;padding-right:0px;padding-bottom:25px;padding-left:0px;">
            <div class="txtTinyMce-wrapper" style="line-height: 1.5; font-size: 12px; font-family: 'Poppins', Arial, Helvetica, sans-serif; color: #ffffff; mso-line-height-alt: 18px;">
            <p style="line-height: 1.5; word-break: break-word; font-family: Poppins, Arial, Helvetica, sans-serif; font-size: 14px; mso-line-height-alt: 21px; margin: 0;"><span style="font-size: 14px;"><strong><span style="">It's free daily news feed provided by Realitywings.com for investors.</span></strong></span></p>
            </div>
            </div>
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
            """



    for i in range(len(df.index)):
        title = df.loc[i]['title']
        url = df.loc[i]['url']
        imgurl=df.loc[i]['urlToImage']
        #publishedAt = df.loc[i]['publishedAt']
        source = df.loc[i]['source'].get('name')
        description = df.loc[i]['description']
        body_html = body_html + f"""
                                    <div style="background-color:transparent;">
                                    <div class="block-grid" style="min-width: 320px; max-width: 640px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: #e9e9e9;">
                                    <div style="border-collapse: collapse;display: table;width: 100%;background-color:#e9e9e9;">
                                    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:640px"><tr class="layout-full-width" style="background-color:#e9e9e9"><![endif]-->
                                    <!--[if (mso)|(IE)]><td align="center" width="640" style="background-color:#e9e9e9;width:640px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:25px;"><![endif]-->
                                    <div class="col num12" style="min-width: 320px; max-width: 640px; display: table-cell; vertical-align: top; width: 640px;">
                                    <div class="col_cont" style="width:100% !important;">
                                    <!--[if (!mso)&(!IE)]><!-->
                                    <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:25px; padding-right: 0px; padding-left: 0px;">
                                    <!--<![endif]-->
                                    <div align="center" class="img-container center autowidth" style="padding-right: 30px;padding-left: 30px;">
                                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 30px;padding-left: 30px;" align="center"><![endif]-->
                                    <div style="font-size:1px;line-height:30px"> </div><img align="center" alt="I'm an image" border="0" class="center autowidth" src="{imgurl}" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 580px; display: block;" title="I'm an image" width="580"/>
                                    <div style="font-size:1px;line-height:30px"> </div>
                                    <!--[if mso]></td></tr></table><![endif]-->
                                    </div>
                                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 30px; padding-top: 25px; padding-bottom: 0px; font-family: Arial, sans-serif"><![endif]-->
                                    <div style="color:#555555;font-family:'Poppins', Arial, Helvetica, sans-serif;line-height:1.2;padding-top:25px;padding-right:0px;padding-bottom:0px;padding-left:30px;">
                                    <div class="txtTinyMce-wrapper" style="line-height: 1.2; font-size: 12px; font-family: 'Poppins', Arial, Helvetica, sans-serif; color: #555555; mso-line-height-alt: 14px;">
                                    <p style="font-size: 14px; line-height: 1.2; word-break: break-word; font-family: Poppins, Arial, Helvetica, sans-serif; mso-line-height-alt: 17px; margin: 0;"><strong><span style="color: #75997e;">{source}</span></strong></p>
                                    </div>
                                    </div>
                                    <!--[if mso]></td></tr></table><![endif]-->
                                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 30px; padding-left: 30px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]-->
                                    <div style="color:#555555;font-family:'Poppins', Arial, Helvetica, sans-serif;line-height:1.2;padding-top:10px;padding-right:30px;padding-bottom:10px;padding-left:30px;">
                                    <div class="txtTinyMce-wrapper" style="line-height: 1.2; font-family: 'Poppins', Arial, Helvetica, sans-serif; font-size: 12px; color: #555555; mso-line-height-alt: 14px;">
                                    <p style="font-size: 24px; line-height: 1.2; text-align: left; word-break: break-word; font-family: Poppins, Arial, Helvetica, sans-serif; mso-line-height-alt: 29px; margin: 0;"><span style="color: #695e8f; font-size: 24px;"><strong>{title}</strong></span></p>
                                    </div>
                                    </div>
                                    <!--[if mso]></td></tr></table><![endif]-->
                                    <table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%">
                                    <tbody>
                                    <tr style="vertical-align: top;" valign="top">
                                    <td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 30px;" valign="top">
                                    <table align="left" border="0" cellpadding="0" cellspacing="0" class="divider_content" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 5px solid #75997E; width: 15%;" valign="top" width="15%">
                                    <tbody>
                                    <tr style="vertical-align: top;" valign="top">
                                    <td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top"><span></span></td>
                                    </tr>
                                    </tbody>
                                    </table>
                                    </td>
                                    </tr>
                                    </tbody>
                                    </table>
                                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 30px; padding-left: 30px; padding-top: 10px; padding-bottom: 10px; font-family: Georgia, serif"><![endif]-->
                                    <div style="color:#3c3c3c;font-family:'Playfair Display', Georgia, serif;line-height:1.5;padding-top:10px;padding-right:30px;padding-bottom:10px;padding-left:30px;">
                                    <div class="txtTinyMce-wrapper" style="line-height: 1.5; font-size: 12px; font-family: 'Playfair Display', Georgia, serif; color: #3c3c3c; mso-line-height-alt: 18px;">
                                    <p style="font-size: 16px; line-height: 1.5; text-align: left; word-break: break-word; font-family: 'Playfair Display', Georgia, serif; mso-line-height-alt: 24px; margin: 0;"><span style="font-size: 16px;">{description} An mea hinc veritus, te tale dolorum eleifend vel.</span></p>
                                    </div>
                                    </div>
                                    <!--[if mso]></td></tr></table><![endif]-->
                                    <div align="left" class="button-container" style="padding-top:10px;padding-right:30px;padding-bottom:10px;padding-left:30px;">
                                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;"><tr><td style="padding-top: 10px; padding-right: 30px; padding-bottom: 10px; padding-left: 30px" align="left"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="{url}" style="height:24pt; width:117.75pt; v-text-anchor:middle;" arcsize="13%" stroke="false" fillcolor="#ed9090"><w:anchorlock/><v:textbox inset="0,0,0,0"><center style="color:#423460; font-family:Arial, sans-serif; font-size:14px"><![endif]--><a href="{url}" style="-webkit-text-size-adjust: none; text-decoration: none; display: inline-block; color: #423460; background-color: #ed9090; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; width: auto; width: auto; border-top: 1px solid #ed9090; border-right: 1px solid #ed9090; border-bottom: 1px solid #ed9090; border-left: 1px solid #ed9090; padding-top: 0px; padding-bottom: 0px; font-family: 'Poppins', Arial, Helvetica, sans-serif; text-align: center; mso-border-alt: none; word-break: keep-all;" target="_blank"><span style="padding-left:20px;padding-right:20px;font-size:14px;display:inline-block;"><span style="font-size: 16px; margin: 0; line-height: 2; word-break: break-word; font-family: Poppins, Arial, Helvetica, sans-serif; mso-line-height-alt: 32px;"><strong><span data-mce-style="font-size: 14px; line-height: 28px;" style="font-size: 14px; line-height: 28px;">Learn More</span></strong></span></span></a>
                                    <!--[if mso]></center></v:textbox></v:roundrect></td></tr></table><![endif]-->
                                    </div>
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
                                    """


    tail_html = """
                    <div style="background-color:transparent;">
                    <div class="block-grid two-up" style="min-width: 320px; max-width: 640px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: #69a4d2;">
                    <div style="border-collapse: collapse;display: table;width: 100%;background-color:#69a4d2;">
                    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:640px"><tr class="layout-full-width" style="background-color:#69a4d2"><![endif]-->
                    <!--[if (mso)|(IE)]><td align="center" width="320" style="background-color:#69a4d2;width:320px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
                    <div class="col num6" style="display: table-cell; vertical-align: top; max-width: 320px; min-width: 318px; width: 320px;">
                    <div class="col_cont" style="width:100% !important;">
                    <!--[if (!mso)&(!IE)]><!-->
                    <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
                    <!--<![endif]-->
                    <div align="left" class="img-container left fixedwidth" style="padding-right: 0px;padding-left: 30px;">
                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 30px;" align="left"><![endif]-->
                    <div style="font-size:1px;line-height:30px"> </div><img alt="Maintained by VAI TECH Solution." border="0" class="left fixedwidth" src="https://vaitech.in/wp-content/uploads/2020/10/vai_FULL.png" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 107px; display: block;" title="Maintained by VAI TECH Solution." width="107"/>
                    <div style="font-size:1px;line-height:25px"> </div>
                    <!--[if mso]></td></tr></table><![endif]-->
                    </div>
                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 30px; padding-top: 10px; padding-bottom: 5px; font-family: Arial, sans-serif"><![endif]-->
                    <div style="color:#ffffff;font-family:'Poppins', Arial, Helvetica, sans-serif;line-height:1.2;padding-top:10px;padding-right:10px;padding-bottom:5px;padding-left:30px;">
                    <div class="txtTinyMce-wrapper" style="line-height: 1.2; font-size: 12px; font-family: 'Poppins', Arial, Helvetica, sans-serif; color: #ffffff; mso-line-height-alt: 14px;">
                    <p style="font-size: 12px; line-height: 1.2; word-break: break-word; text-align: left; font-family: Poppins, Arial, Helvetica, sans-serif; mso-line-height-alt: 14px; margin: 0;"><span style="font-size: 12px;"><strong>123, xyz, address</strong></span></p>
                    </div>
                    </div>
                    <!--[if mso]></td></tr></table><![endif]-->
                    <table cellpadding="0" cellspacing="0" class="social_icons" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;" valign="top" width="100%">
                    <tbody>
                    <tr style="vertical-align: top;" valign="top">
                    <td style="word-break: break-word; vertical-align: top; padding-top: 5px; padding-right: 15px; padding-bottom: 20px; padding-left: 25px;" valign="top">
                    <table align="left" cellpadding="0" cellspacing="0" class="social_table" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-tspace: 0; mso-table-rspace: 0; mso-table-bspace: 0; mso-table-lspace: 0;" valign="top">
                    <tbody>
                    <tr align="left" style="vertical-align: top; display: inline-block; text-align: left;" valign="top">
                    <td style="word-break: break-word; vertical-align: top; padding-bottom: 0; padding-right: 4px; padding-left: 0px;" valign="top"><a href="https://www.facebook.com/" target="_blank"><img alt="Facebook" height="32" src="images/facebook2x.png" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; display: block;" title="Facebook" width="32"/></a></td>
                    <td style="word-break: break-word; vertical-align: top; padding-bottom: 0; padding-right: 4px; padding-left: 0px;" valign="top"><a href="https://instagram.com/" target="_blank"><img alt="Instagram" height="32" src="images/instagram2x.png" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; display: block;" title="Instagram" width="32"/></a></td>
                    <td style="word-break: break-word; vertical-align: top; padding-bottom: 0; padding-right: 4px; padding-left: 0px;" valign="top"><a href="https://www.pinterest.com/" target="_blank"><img alt="Pinterest" height="32" src="images/pinterest2x.png" style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; display: block;" title="Pinterest" width="32"/></a></td>
                    </tr>
                    </tbody>
                    </table>
                    </td>
                    </tr>
                    </tbody>
                    </table>
                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 60px; padding-left: 30px; padding-top: 10px; padding-bottom: 25px; font-family: Arial, sans-serif"><![endif]-->
                    <div style="color:#ffffff;font-family:'Poppins', Arial, Helvetica, sans-serif;line-height:1.2;padding-top:10px;padding-right:60px;padding-bottom:25px;padding-left:30px;">
                    <div class="txtTinyMce-wrapper" style="line-height: 1.2; font-size: 12px; font-family: 'Poppins', Arial, Helvetica, sans-serif; color: #ffffff; mso-line-height-alt: 14px;">
                    <p style="font-size: 14px; line-height: 1.2; word-break: break-word; text-align: left; font-family: Poppins, Arial, Helvetica, sans-serif; mso-line-height-alt: 17px; margin: 0;">If you no longer wish to receive access to cool, free stuff, you can <span style="color: #ed9090;"><u>unsubscribe here</u></span>.</p>
                    </div>
                    </div>
                    <!--[if mso]></td></tr></table><![endif]-->
                    <!--[if (!mso)&(!IE)]><!-->
                    </div>
                    <!--<![endif]-->
                    </div>
                    </div>
                    <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
                    <!--[if (mso)|(IE)]></td><td align="center" width="320" style="background-color:#69a4d2;width:320px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
                    <div class="col num6" style="display: table-cell; vertical-align: top; max-width: 320px; min-width: 318px; width: 320px;">
                    <div class="col_cont" style="width:100% !important;">
                    <!--[if (!mso)&(!IE)]><!-->
                    <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
                    <!--<![endif]-->
                    <div></div>
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
                    <div class="block-grid" style="min-width: 320px; max-width: 640px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: transparent;">
                    <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
                    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:640px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
                    <!--[if (mso)|(IE)]><td align="center" width="640" style="background-color:transparent;width:640px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
                    <div class="col num12" style="min-width: 320px; max-width: 640px; display: table-cell; vertical-align: top; width: 640px;">
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