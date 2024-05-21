# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html

import dashscope


def sample_sync_call_streaming():
    prompt_text = '用萝卜、土豆、茄子做饭，给我个菜谱。'
    response_generator = dashscope.Generation.call(
        model='qwen-turbo',
        prompt=prompt_text,
        stream=True,
        top_p=0.8)

    head_idx = 0
    for resp in response_generator:
        paragraph = resp.output['text']
        print("\r%s" % paragraph[head_idx:len(paragraph)], end='')
        if(paragraph.rfind('\n') != -1):
            head_idx = paragraph.rfind('\n') + 1


sample_sync_call_streaming()