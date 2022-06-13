from airium import Airium

def export_chart_to_html(fig, height, filename, describtion_list, insight_list):
    fig.update_layout(
        title_text='',
        margin=dict(l=50, r=50, t=50, b=50, pad=4),
        height=height
    )

    a = Airium()
    # Generating HTML file
    a('<!DOCTYPE html>')
    with a.html(lang="en"):
        with a.head():
            a.meta(charset="utf-8")
            a.title(_t="Example: How to use Airium library")
        with a.body():
            with a.h1(id="chart_name"):
                a("Hello Finxters")
            with a.h2(id="chart_discussion"):
                a("Description")
            with a.ul():
                for item in describtion_list:
                    with a.li():
                        a(item)
            with a.h2(id="chart_insight"):
                a("Insight")
            with a.ul():
                for item in insight_list:
                    with a.li():
                        a(item)
            with a.div():
                
                a(fig.to_html(full_html=False, include_plotlyjs='cdn'))
    # Casting the file to a string to extract the value
    html = str(a)
    # Casting the file to UTF-8 encoded bytes:
    # html_bytes = bytes(a)
    with open(filename, 'wb') as f:
        f.write(bytes(html, encoding='utf8'))