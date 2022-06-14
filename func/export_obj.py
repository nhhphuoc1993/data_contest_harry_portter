from airium import Airium

def render_list_html(a: Airium, imput_list):
    if imput_list and type(imput_list) is list:
        with a.ul():
            for item in imput_list:
                if item:
                    with a.li():
                        if type(item) is dict:
                            # Get first key-value pair of the dictionary
                            first_pair = list(item.items())[0]
                            a(first_pair[0])
                            value = first_pair[1]
                            if type(value) is list:
                                render_list_html(a, value)
                            else:
                                a(value)
                        else:
                            a(item)
    return a

def export_chart_to_html(fig, height, path_to_filename, chart_id, chart_title, describtion_list, insight_list):
    fig.update_layout(
        title_text='',
        margin=dict(l=50, r=50, t=50, b=50, pad=4)
    )

    a = Airium()
    # Generating HTML file
    a('<!DOCTYPE html>')
    with a.html(lang="en"):
        with a.head():
            a.meta(charset="utf-8")
            a.title(_t=chart_title)
        with a.body():
            with a.h1(id="chart_name"):
                a(chart_title)
            with a.h2(id="chart_discussion"):
                a("Description")
            render_list_html(a, describtion_list)
            with a.h2(id="chart_insight"):
                a("Insight")
            render_list_html(a, insight_list)
            with a.div():
                a(fig.to_html(
                    full_html=False, 
                    include_plotlyjs='cdn',
                    default_height=height if height else '100%',
                    div_id=chart_id
                ))
    # Casting the file to a string to extract the value
    html = str(a)
    # Casting the file to UTF-8 encoded bytes:
    # html_bytes = bytes(a)
    with open(path_to_filename, 'wb') as f:
        f.write(bytes(html, encoding='utf8'))