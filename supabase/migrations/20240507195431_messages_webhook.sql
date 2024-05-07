create or replace function firebase_send_message()
returns trigger
language plpgsql
as $$
begin
    perform net.http_post(
        url := 'https://sendnotifications-tb6tbuyisq-ew.a.run.app',
        body := jsonb_build_object('type', TG_OP, 'table', TG_TABLE_NAME, 'record', row_to_json(new), 'schema', TG_TABLE_SCHEMA),
        headers := '{"Content-Type": "application/json"}'::jsonb,
        timeout_milliseconds := 5000
    );
    return new;
end;
$$;

drop trigger if exists "firebase-send-message-webhook" on public.messages;
create trigger "firebase-send-message-webhook"
after insert on public.messages
for each row
execute function firebase_send_message();